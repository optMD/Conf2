"""CLI apt-depgraph: параметры и прямые зависимости из Packages.gz."""

import argparse
import dataclasses
import os
import re
import subprocess
import sys

MODE_REPO = "repo"
MODE_TEST = "test"
MODES = (MODE_REPO, MODE_TEST)
DEFAULT_OUTPUT = "graph.png"
PNG_SUFFIX = ".png"
URL_PREFIXES = ("http://", "https://")
REPO_PACKAGE_PATTERN = re.compile(r"^[a-z0-9][a-z0-9.+\-]+$")
TEST_NODE_PATTERN = re.compile(r"^[A-Z]$")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FETCH_BINARY = os.path.join(ROOT, "build", "bin", "fetch")
FIELD_PACKAGE = "Package"
FIELDS_DEPENDS = ("Depends", "Pre-Depends")
FIELD_SEPARATOR = ":"
GROUP_SEPARATOR = ","
ALT_SEPARATOR = "|"
ARCH_SEPARATOR = ":"
EXIT_CONFIG_ERROR = 2
EXIT_RUNTIME_ERROR = 1


class ConfigError(ValueError):
    """Некорректное значение параметра командной строки."""


class PipelineError(RuntimeError):
    """Ошибка при загрузке или разборе данных о зависимостях."""


@dataclasses.dataclass(frozen=True)
class Config:
    """Все настраиваемые пользователем параметры запуска."""

    package: str
    source: str
    mode: str
    output: str
    direct: bool
    reverse: bool


def build_parser():
    """Создаёт парсер опций командной строки."""
    parser = argparse.ArgumentParser(
        prog="apt-depgraph",
        description="Визуализация графа зависимостей пакета Ubuntu (apt).",
    )
    parser.add_argument(
        "package", help="имя анализируемого пакета (буква в тестовом режиме)"
    )
    parser.add_argument(
        "source",
        help="URL файла Packages.gz или путь к тестовому файлу графа",
    )
    parser.add_argument(
        "--mode",
        choices=MODES,
        default=MODE_REPO,
        help="repo — реальный репозиторий, test — тестовый граф из файла",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT,
        help="имя PNG-файла с изображением графа",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--direct",
        action="store_true",
        help="вывести только прямые зависимости",
    )
    group.add_argument(
        "--reverse",
        action="store_true",
        help="вывести обратные зависимости (кто зависит от пакета)",
    )
    return parser


def check_package(name, mode):
    """Проверяет имя пакета с учётом режима работы."""
    if mode == MODE_TEST:
        if not TEST_NODE_PATTERN.match(name):
            raise ConfigError(
                f"в тестовом режиме имя — одна заглавная буква: {name!r}"
            )
        return
    if not REPO_PACKAGE_PATTERN.match(name):
        raise ConfigError(f"некорректное имя пакета apt: {name!r}")


def check_source(source, mode):
    """Проверяет URL репозитория или путь к тестовому файлу."""
    if mode == MODE_TEST:
        if not os.path.isfile(source):
            raise ConfigError(f"тестовый файл не найден: {source}")
        return
    if not source.startswith(URL_PREFIXES):
        raise ConfigError(f"ожидается URL http(s) для репозитория: {source}")


def check_output(output):
    """Проверяет имя выходного PNG-файла и существование его папки."""
    if not output.lower().endswith(PNG_SUFFIX):
        raise ConfigError(f"выходной файл должен быть .png: {output}")
    directory = os.path.dirname(os.path.abspath(output))
    if not os.path.isdir(directory):
        raise ConfigError(f"папка для вывода не существует: {directory}")


def load_config(argv):
    """Разбирает аргументы, проверяет их и возвращает Config."""
    args = build_parser().parse_args(argv)
    check_package(args.package, args.mode)
    check_source(args.source, args.mode)
    check_output(args.output)
    return Config(
        package=args.package,
        source=args.source,
        mode=args.mode,
        output=args.output,
        direct=args.direct,
        reverse=args.reverse,
    )


def run_command(args):
    """Запускает внешнюю программу и возвращает её stdout."""
    try:
        result = subprocess.run(
            args, capture_output=True, text=True, check=False
        )
    except OSError as error:
        raise PipelineError(
            f"не удалось запустить {args[0]}: {error} "
            "(соберите компоненты: ./run.sh build)"
        ) from error
    if result.returncode != 0:
        message = result.stderr.strip() or f"{args[0]} завершился с ошибкой"
        raise PipelineError(message)
    return result.stdout


def fetch_index(url, binary=FETCH_BINARY):
    """Скачивает Packages.gz через Go-загрузчик и возвращает его текст."""
    return run_command([binary, url])


def parse_dependency_group(group):
    """Возвращает имя первой альтернативы группы без версии и архитектуры."""
    first = group.split(ALT_SEPARATOR, 1)[0].strip()
    if not first:
        return None
    name = first.split()[0]
    return name.split(ARCH_SEPARATOR, 1)[0]


def parse_dependency_field(value):
    """Разбирает поле Depends или Pre-Depends в список имён пакетов."""
    names = []
    for group in value.split(GROUP_SEPARATOR):
        name = parse_dependency_group(group)
        if name:
            names.append(name)
    return names


def parse_packages(text):
    """Читает индекс Packages и возвращает {пакет: [прямые зависимости]}."""
    graph = {}
    name = None
    deps = []
    for line in text.splitlines() + [""]:
        if not line.strip():
            if name is not None:
                graph[name] = list(dict.fromkeys(deps))
            name, deps = None, []
            continue
        if line[0] in " \t":
            continue
        key, separator, value = line.partition(FIELD_SEPARATOR)
        if not separator:
            continue
        key = key.strip()
        if key == FIELD_PACKAGE:
            name = value.strip()
        elif key in FIELDS_DEPENDS:
            deps.extend(parse_dependency_field(value))
    return graph


def direct_dependencies(graph, package):
    """Возвращает прямые зависимости пакета или ошибку, если его нет."""
    if package not in graph:
        raise PipelineError(f"пакет не найден в индексе: {package}")
    return graph[package]


def run_direct_dependencies(config):
    """Возвращает прямые зависимости пакета из репозитория."""
    if config.mode == MODE_TEST:
        raise PipelineError("тестовый режим появится на этапе 3")
    graph = parse_packages(fetch_index(config.source))
    return direct_dependencies(graph, config.package)


def main(argv=None):
    """Запускает приложение и возвращает код завершения."""
    argv = sys.argv[1:] if argv is None else argv
    try:
        config = load_config(argv)
    except ConfigError as error:
        print(f"ошибка: {error}", file=sys.stderr)
        return EXIT_CONFIG_ERROR
    try:
        for dep in run_direct_dependencies(config):
            print(dep)
    except PipelineError as error:
        print(f"ошибка: {error}", file=sys.stderr)
        return EXIT_RUNTIME_ERROR
    return 0


if __name__ == "__main__":
    sys.exit(main())

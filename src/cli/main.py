"""CLI-инструмент визуализации графа зависимостей пакетов Ubuntu (apt)."""

import argparse
import dataclasses
import os
import re
import sys

MODE_REPO = "repo"
MODE_TEST = "test"
MODES = (MODE_REPO, MODE_TEST)
DEFAULT_OUTPUT = "graph.png"
PNG_SUFFIX = ".png"
URL_PREFIXES = ("http://", "https://")
REPO_PACKAGE_PATTERN = re.compile(r"^[a-z0-9][a-z0-9.+\-]+$")
TEST_NODE_PATTERN = re.compile(r"^[A-Z]$")
EXIT_CONFIG_ERROR = 2


class ConfigError(ValueError):
    """Некорректное значение параметра командной строки."""


@dataclasses.dataclass(frozen=True)
class Config:
    """Все настраиваемые пользователем параметры запуска."""

    package: str
    source: str
    mode: str
    output: str
    direct: bool
    reverse: bool

    def as_pairs(self):
        """Возвращает пары «ключ, значение» для вывода."""
        return [
            ("package", self.package),
            ("source", self.source),
            ("mode", self.mode),
            ("output", self.output),
            ("direct", str(self.direct).lower()),
            ("reverse", str(self.reverse).lower()),
        ]


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
        help="repo — реальный репозиторий, test — граф из файла",
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


def print_settings(config):
    """Выводит параметры запуска в формате ключ-значение."""
    for key, value in config.as_pairs():
        print(f"{key}: {value}")


def main(argv=None):
    """Запускает приложение и возвращает код завершения."""
    argv = sys.argv[1:] if argv is None else argv
    try:
        config = load_config(argv)
    except ConfigError as error:
        print(f"ошибка: {error}", file=sys.stderr)
        return EXIT_CONFIG_ERROR
    print_settings(config)
    return 0


if __name__ == "__main__":
    sys.exit(main())

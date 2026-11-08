"""CLI apt-depgraph: параметры, данные о зависимостях и обход графа."""

import argparse
import collections
import dataclasses
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

MODE_REPO = "repo"
MODE_TEST = "test"
MODES = (MODE_REPO, MODE_TEST)

DEFAULT_OUTPUT = "graph.png"
PNG_SUFFIX = ".png"
DIRECT_DEPTH = 1

URL_PREFIXES = ("http://", "https://")
HTTP_TIMEOUT = 120
REPO_PACKAGE_PATTERN = re.compile(r"^[a-z0-9][a-z0-9.+\-]+$")

TEST_NODE_PATTERN = re.compile(r"^[A-Z]$")
NODE_SEPARATOR = ":"

FIELD_PACKAGE = "Package"
FIELDS_DEPENDS = ("Depends", "Pre-Depends")
FIELD_SEPARATOR = ":"
GROUP_SEPARATOR = ","
ALT_SEPARATOR = "|"
ARCH_SEPARATOR = ":"

UNPACK_BINARY = os.path.join(ROOT, "build", "bin", "unpack")
RENDER_BINARY = os.path.join(ROOT, "build", "bin", "render")
DOT_BINARY = "dot"
JAVA_COMMAND = "java"
REVERSE_CLASSPATH = os.path.join(ROOT, "build", "java")
REVERSE_CLASS = "Reverse"
DOTWRAP_CLASSPATH = os.path.join(ROOT, "build", "dotwrap", "dotwrap.jar")
DOTWRAP_CLASS = "dotwrap.DotWrapKt"

EXIT_CONFIG_ERROR = 2
EXIT_RUNTIME_ERROR = 1


class ConfigError(ValueError):
    """Некорректное значение параметра командной строки."""


class PipelineError(RuntimeError):
    """Ошибка при загрузке данных, разборе или обходе графа."""


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


def run_command(args, stdin_bytes=b""):
    """Запускает программу с stdin_bytes и возвращает stdout как текст."""
    try:
        result = subprocess.run(
            args, input=stdin_bytes, capture_output=True, check=False
        )
    except OSError as error:
        raise PipelineError(
            f"не удалось запустить {args[0]}: {error} "
            "(соберите компоненты: ./run.sh build)"
        ) from error
    if result.returncode != 0:
        message = result.stderr.strip() or f"{args[0]} завершился с ошибкой"
        raise PipelineError(message)
    return result.stdout.decode("utf-8")


def fetch_index(url):
    """Скачивает Packages.gz по URL и возвращает его распакованный текст."""
    try:
        with urllib.request.urlopen(url, timeout=HTTP_TIMEOUT) as response:
            packed = response.read()
    except (OSError, ValueError) as error:
        raise PipelineError(f"не удалось скачать {url}: {error}") from error
    return run_command([UNPACK_BINARY], stdin_bytes=packed)


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


def parse_test_line(line, number):
    """Разбирает строку «A: B C» в пару (узел, список зависимостей)."""
    name, separator, rest = line.partition(NODE_SEPARATOR)
    if not separator:
        raise PipelineError(f"строка {number}: ожидается формат «A: B C»")
    tokens = [name.strip()] + rest.split()
    for token in tokens:
        if not TEST_NODE_PATTERN.match(token):
            raise PipelineError(
                f"строка {number}: имя должно быть одной заглавной буквой: "
                f"{token!r}"
            )
    return tokens[0], tokens[1:]


def load_test_graph(path):
    """Читает тестовый граф из файла и возвращает {узел: [зависимости]}."""
    graph = {}
    with open(path, encoding="utf-8") as handle:
        for number, raw in enumerate(handle, start=1):
            line = raw.strip()
            if line:
                node, deps = parse_test_line(line, number)
                graph.setdefault(node, []).extend(deps)
    if not graph:
        raise PipelineError(f"тестовый граф пуст: {path}")
    return graph


def ensure_package(graph, package):
    """Проверяет, что пакет есть в графе как узел или как зависимость."""
    known = set(graph)
    for deps in graph.values():
        known.update(deps)
    if package not in known:
        raise PipelineError(f"пакет не найден: {package}")


def traverse(graph, root, max_depth=None):
    """Обход в ширину без рекурсии.

    Возвращает узлы в порядке обнаружения и рёбра (от, к). Уже посещённые
    узлы не ставятся в очередь повторно, поэтому циклы завершаются.
    """
    depth = {root: 0}
    edges = []
    seen_edges = set()
    queue = collections.deque([root])
    while queue:
        current = queue.popleft()
        level = depth[current]
        if max_depth is not None and level >= max_depth:
            continue
        for nxt in graph.get(current, []):
            edge = (current, nxt)
            if edge not in seen_edges:
                seen_edges.add(edge)
                edges.append(edge)
            if nxt not in depth:
                depth[nxt] = level + 1
                queue.append(nxt)
    return list(depth), edges


def load_graph(config):
    """Возвращает граф из тестового файла или из репозитория."""
    if config.mode == MODE_TEST:
        return load_test_graph(config.source)
    return parse_packages(fetch_index(config.source))


def reverse_graph(graph):
    """Обращает рёбра графа через Java-компонент и возвращает новый граф."""
    lines = [f"{src} {dst}" for src, deps in graph.items() for dst in deps]
    text = run_command(
        [JAVA_COMMAND, "-cp", REVERSE_CLASSPATH, REVERSE_CLASS],
        stdin_bytes=("\n".join(lines) + "\n").encode("utf-8"),
    )
    reversed_graph = {}
    for line in text.splitlines():
        src, dst = line.split()
        reversed_graph.setdefault(src, []).append(dst)
    return reversed_graph


def graph_lines(nodes, edges):
    """Превращает узлы и рёбра в строки NODE/EDGE для компонента Rust."""
    lines = [f"NODE {name}" for name in nodes]
    lines.extend(f"EDGE {src} {dst}" for src, dst in edges)
    return "\n".join(lines) + "\n"


def to_dot(nodes, edges):
    """Возвращает текст Graphviz DOT: Rust строит строки, Kotlin оборачивает."""
    body = run_command(
        [RENDER_BINARY], stdin_bytes=graph_lines(nodes, edges).encode("utf-8")
    )
    return run_command(
        [JAVA_COMMAND, "-cp", DOTWRAP_CLASSPATH, DOTWRAP_CLASS],
        stdin_bytes=body.encode("utf-8"),
    )


def render_png(dot_text, output):
    """Сохраняет DOT рядом с PNG и вызывает dot для изображения."""
    with open(os.path.splitext(output)[0] + ".dot", "w", encoding="utf-8") as h:
        h.write(dot_text)
    try:
        subprocess.run(
            [DOT_BINARY, "-Tpng", "-o", output],
            input=dot_text.encode("utf-8"),
            check=True,
            capture_output=True,
        )
    except OSError as error:
        raise PipelineError(f"не удалось запустить dot: {error}") from error
    except subprocess.CalledProcessError as error:
        message = error.stderr.decode("utf-8", "replace").strip()
        raise PipelineError(f"dot завершился с ошибкой: {message}") from error


def find_subgraph(config):
    """Возвращает узлы без корня и рёбра обхода (или обратного) графа."""
    graph = load_graph(config)
    ensure_package(graph, config.package)
    if config.reverse:
        graph = reverse_graph(graph)
    max_depth = DIRECT_DEPTH if config.direct else None
    nodes, edges = traverse(graph, config.package, max_depth)
    return [node for node in nodes if node != config.package], edges


def main(argv=None):
    """Запускает приложение и возвращает код завершения."""
    argv = sys.argv[1:] if argv is None else argv
    try:
        config = load_config(argv)
    except ConfigError as error:
        print(f"ошибка: {error}", file=sys.stderr)
        return EXIT_CONFIG_ERROR
    try:
        nodes, edges = find_subgraph(config)
        for node in nodes:
            print(node)
        render_png(to_dot([config.package] + nodes, edges), config.output)
    except PipelineError as error:
        print(f"ошибка: {error}", file=sys.stderr)
        return EXIT_RUNTIME_ERROR
    return 0


if __name__ == "__main__":
    sys.exit(main())

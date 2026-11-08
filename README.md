# apt-depgraph

Инструмент визуализации графа зависимостей пакета Ubuntu (формат apt).
Получение зависимостей выполнено без менеджеров пакетов и сторонних
библиотек.

## Общее описание

Инструмент читает зависимости пакета из файла `Packages.gz` репозитория
Ubuntu или из тестового файла графа, выводит узлы обхода на экран и
сохраняет граф в PNG через Graphviz.

Основная логика написана на Python. Остальные языки выполняют мелкие
подзадачи через stdin/stdout:

- Go (`src/unpack`) — распаковка gzip;
- Java (`src/reverse`) — обращение рёбер для `--reverse`;
- Rust (`src/render`) — строки `NODE`/`EDGE` превращаются в строки DOT;
- Kotlin (`src/dotwrap`) — оборачивает строки в блок `digraph deps { … }`;
- C# (`src/names`) — извлекает имена из строк `  Depends: …` вывода apt-cache;
- Node.js (`src/uniq`) — убирает повторы и сортирует имена.

## Функции

Функции Python (`src/cli/main.py`):

| Функция | Что делает |
|---|---|
| `build_parser` | описывает параметры командной строки |
| `check_package` | проверяет имя пакета: в repo — имя apt, в test — одна заглавная буква |
| `check_source` | проверяет URL `http(s)` (repo) или существование файла (test) |
| `check_output` | проверяет расширение `.png` и существование папки вывода |
| `load_config` | разбирает аргументы, проверяет их и возвращает `Config` |
| `run_command` | запускает внешний компонент, передаёт stdin и возвращает stdout |
| `fetch_index` | скачивает `Packages.gz` через `urllib` и распаковывает его через `build/bin/unpack` |
| `parse_dependency_group` | берёт первую альтернативу `|` и отбрасывает версию и архитектуру |
| `parse_dependency_field` | разбирает поля `Depends` и `Pre-Depends` |
| `parse_packages` | превращает текст `Packages` в словарь «пакет → зависимости» |
| `parse_test_line` | разбирает строку тестового файла `A: B C` |
| `load_test_graph` | читает тестовый граф из файла |
| `ensure_package` | проверяет, что пакет есть в графе |
| `traverse` | обход в ширину без рекурсии, возвращает узлы и рёбра |
| `load_graph` | выбирает источник графа по режиму `--mode` |
| `reverse_graph` | обращает рёбра графа через Java-компонент `src/reverse` |
| `graph_lines` | превращает узлы и рёбра в строки `NODE`/`EDGE` |
| `to_dot` | Rust строит строки графа, Kotlin оборачивает их в `digraph` |
| `render_png` | сохраняет `.dot` рядом с PNG и вызывает `dot -Tpng` |
| `find_subgraph` | возвращает узлы без корня и рёбра обхода (с учётом `--reverse`) |
| `main` | запускает приложение и возвращает код завершения |

## Настройки

| Параметр | Значение |
|---|---|
| `package` | имя анализируемого пакета (в тестовом режиме — одна заглавная буква) |
| `source` | URL файла `Packages.gz` или путь к тестовому файлу |
| `--mode {repo,test}` | `repo` — реальный репозиторий (по умолчанию), `test` — граф из файла |
| `-o, --output FILE` | имя PNG-файла, по умолчанию `graph.png`; рядом пишется `.dot` |
| `--direct` | вывести только прямые зависимости |
| `--reverse` | вывести обратные зависимости (кто зависит от пакета) |

Коды завершения: `0` — успех, `1` — ошибка выполнения (граф, сеть,
отсутствующий пакет), `2` — некорректный параметр.

Служебные команды `run.sh`:

| Команда | Что делает |
|---|---|
| `./run.sh names <файл>` | печатает имена из строк `  Depends: …` (C#) |
| `./run.sh uniq <файл>` | печатает уникальные отсортированные имена (Node.js) |
| `./run.sh apt-compare <пакет>` | прямые зависимости из `apt-cache depends` в Docker |

## Сборка и тесты

```sh
./run.sh build   # собрать все компоненты в build/
./run.sh test    # собрать и прогнать тесты Python
```

Требуются Go, JDK, Rust (rustc), Python 3, Graphviz (`dot`), Node.js,
.NET SDK и Kotlin (kotlinc). Если .NET, Node или Kotlin не установлены,
`build` пропускает соответствующий компонент с предупреждением.
Для `apt-compare` нужен запущенный Docker.

Тесты: `tests/cli` (Python, 25 тестов), тестовые графы — в `tests/data`.
Компоненты на Go, Java, Rust, C#, Kotlin и Node.js отдельных тестов не
имеют.

## Примеры использования

Тестовый граф с циклом:

```sh
./run.sh A tests/data/cycle.txt --mode test
```

Обратные зависимости в тестовом графе:

```sh
./run.sh C tests/data/chain.txt --mode test --reverse
```

Прямые зависимости `curl` из репозитория Ubuntu с PNG:

```sh
./run.sh curl https://archive.ubuntu.com/ubuntu/dists/noble/main/binary-amd64/Packages.gz --direct -o build/curl.png
```

Три пакета (curl, wget, git) и список `apt-cache depends`:

```sh
for p in curl wget git; do
  ./run.sh $p https://archive.ubuntu.com/ubuntu/dists/noble/main/binary-amd64/Packages.gz --direct -o build/$p.png
  ./run.sh apt-compare $p > build/$p.apt.txt
done
```

Результаты (`--direct`, Ubuntu noble):

| Пакет | Наши прямые зависимости | apt-cache | Совпало |
|---|---|---|---|
| curl | libc6, libcurl4t64, zlib1g | 3 | 3 |
| wget | libc6, libidn2-0, libpcre2-8-0, libpsl5t64, libssl3t64, libuuid1, zlib1g | 7 | 7 |
| git | libc6, libcurl3t64-gnutls, libexpat1, libpcre2-8-0, zlib1g, perl, liberror-perl, git-man | 8 | 8 |

Расхождения возможны из-за первой альтернативы `|` (мы берём первую),
версий и рекомендаций: `Recommends` и `Suggests` не учитываются.

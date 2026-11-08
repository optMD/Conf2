#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="$ROOT/src/cli"

build() {
  mkdir -p "$ROOT/build/bin"
  (cd "$ROOT" && go build -o "$ROOT/build/bin/fetch" ./src/fetch)
}

test_all() {
  (cd "$ROOT" && go test ./src/fetch/...)
  python3 -m unittest discover -s "$ROOT/tests/cli" -t "$ROOT/tests/cli" -p 'test_*.py'
}

case "${1:-}" in
  test)
    build
    test_all
    ;;
  build)
    build
    ;;
  *)
    build
    python3 "$ROOT/src/cli/main.py" "$@"
    ;;
esac

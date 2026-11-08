#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="$ROOT/src/cli"

build() {
  mkdir -p "$ROOT/build/bin"
  (cd "$ROOT" && go build -o "$ROOT/build/bin/unpack" ./src/unpack)
  mkdir -p "$ROOT/build/java"
  javac -d "$ROOT/build/java" "$ROOT/src/reverse/Reverse.java"
}

test_all() {
  (cd "$ROOT" && go test ./src/unpack/...)
  javac -d "$ROOT/build/java" "$ROOT/src/reverse/Reverse.java" \
    "$ROOT/tests/reverse/ReverseTest.java"
  java -cp "$ROOT/build/java" ReverseTest
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

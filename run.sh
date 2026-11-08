#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="$ROOT/src/cli"
cd "$ROOT"

APT_FLAGS="--no-recommends --no-suggests --no-conflicts"
APT_FLAGS="$APT_FLAGS --no-breaks --no-replaces --no-enhances"

case "${1:-}" in
  build | test | clean)
    make -s "$1"
    ;;
  apt-compare)
    shift
    make -s build
    docker run --rm ubuntu:24.04 sh -c \
      'apt-get update -qq >/dev/null 2>&1 && apt-cache depends '"$APT_FLAGS"' "$1"' \
      sh "$1" \
      | dotnet build/names/Names.dll \
      | node src/uniq/uniq.js
    ;;
  *)
    make -s build
    python3 "$ROOT/src/cli/main.py" "$@"
    ;;
esac

# Сборка компонентов apt-depgraph. Пересобирается только изменённое.
# Если компилятор не установлен, компонент пропускается с предупреждением.

BUILD := build
PY_TESTS := tests/cli

UNPACK  := $(BUILD)/bin/unpack
RENDER  := $(BUILD)/bin/render
REVERSE := $(BUILD)/java/Reverse.class
DOTWRAP := $(BUILD)/dotwrap/dotwrap.jar
NAMES   := $(BUILD)/names/Names.dll

WARN = echo "предупреждение: $(1) не найден, компонент пропущен" >&2

.PHONY: build test clean

build: $(UNPACK) $(RENDER) $(REVERSE) $(DOTWRAP) $(NAMES)

$(UNPACK): src/unpack/main.go
	@mkdir -p $(dir $@)
	go build -o $@ ./src/unpack

$(RENDER): src/render/main.rs
	@mkdir -p $(dir $@)
	rustc --edition 2021 -O -o $@ $<

$(REVERSE): src/reverse/Reverse.java
	@mkdir -p $(BUILD)/java
	javac -d $(BUILD)/java $<

$(DOTWRAP): src/dotwrap/DotWrap.kt
	@mkdir -p $(dir $@)
	@if command -v kotlinc >/dev/null 2>&1; then \
		kotlinc $< -include-runtime -d $@; \
	else $(call WARN,kotlinc); fi

$(NAMES): src/names/Program.cs src/names/Names.csproj
	@if command -v dotnet >/dev/null 2>&1; then \
		dotnet build src/names/Names.csproj -c Release -o $(BUILD)/names >/dev/null; \
	else $(call WARN,dotnet); fi

test: build
	PYTHONPATH=src/cli python3 -m unittest discover -s $(PY_TESTS) -t $(PY_TESTS) -p 'test_*.py'

clean:
	rm -rf $(BUILD)

"""Тесты CLI: конфигурация, проверка параметров и разбор Packages."""

import contextlib
import io
import os
import tempfile
import unittest

import main as cli

SAMPLE_INDEX = """Package: curl
Depends: libc6 (>= 2.34), libcurl4 (= 7.81.0), libssl3 | libgnutls30
Pre-Depends: dpkg (>= 1.1)

Package: libc6
Depends: libgcc-s1:amd64
"""


class LoadConfigTest(unittest.TestCase):
    """Разбор и проверка аргументов командной строки."""

    def test_repo_mode_defaults(self):
        """По умолчанию — режим repo, вывод graph.png, флаги выключены."""
        config = cli.load_config(["curl", "https://example.com/Packages.gz"])
        self.assertEqual(config.mode, cli.MODE_REPO)
        self.assertEqual(config.output, cli.DEFAULT_OUTPUT)
        self.assertFalse(config.direct)
        self.assertFalse(config.reverse)

    def test_invalid_package_name_is_rejected(self):
        """Имя с недопустимыми символами даёт ошибку конфигурации."""
        with self.assertRaises(cli.ConfigError):
            cli.load_config(["Curl*", "https://example.com/Packages.gz"])

    def test_test_mode_requires_uppercase_letter(self):
        """В тестовом режиме пакет — одна заглавная буква."""
        with self.assertRaises(cli.ConfigError):
            cli.load_config(["a", "x.txt", "--mode", "test"])

    def test_repo_source_must_be_http_url(self):
        """В режиме репозитория источник обязан быть URL."""
        with self.assertRaises(cli.ConfigError):
            cli.load_config(["curl", "/local/Packages.gz"])

    def test_test_mode_missing_file_is_rejected(self):
        """В тестовом режиме несуществующий файл даёт ошибку."""
        with self.assertRaises(cli.ConfigError):
            cli.load_config(["A", "/no/such/file", "--mode", "test"])

    def test_output_must_be_png(self):
        """Выходной файл обязан иметь расширение .png."""
        with self.assertRaises(cli.ConfigError):
            cli.load_config(
                ["curl", "https://example.com/Packages.gz", "-o", "x.svg"]
            )

    def test_output_directory_must_exist(self):
        """Папка вывода должна существовать."""
        with self.assertRaises(cli.ConfigError):
            cli.load_config(
                ["curl", "https://example.com/Packages.gz",
                 "-o", "/no/such/dir/graph.png"]
            )

    def test_direct_and_reverse_are_exclusive(self):
        """Флаги --direct и --reverse нельзя указывать вместе."""
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit):
                cli.load_config(
                    ["curl", "https://example.com/Packages.gz",
                     "--direct", "--reverse"]
                )

    def test_test_mode_accepts_existing_file(self):
        """Существующий файл приемлем в тестовом режиме."""
        fd, path = tempfile.mkstemp(suffix=".txt")
        os.write(fd, b"A: B\n")
        os.close(fd)
        try:
            config = cli.load_config(["A", path, "--mode", "test"])
            self.assertEqual(config.package, "A")
        finally:
            os.unlink(path)


class ParsePackagesTest(unittest.TestCase):
    """Разбор индекса Packages в список прямых зависимостей."""

    def test_keeps_first_alternative_and_strips_versions(self):
        """Берётся первая альтернатива, версии и архитектура убираются."""
        graph = cli.parse_packages(SAMPLE_INDEX)
        self.assertEqual(
            graph["curl"], ["libc6", "libcurl4", "libssl3", "dpkg"]
        )

    def test_strips_architecture_suffix(self):
        """Суффикс архитектуры вида :amd64 удаляется."""
        graph = cli.parse_packages(SAMPLE_INDEX)
        self.assertEqual(graph["libc6"], ["libgcc-s1"])

    def test_unknown_package_is_an_error(self):
        """Пакет, которого нет в индексе, даёт ошибку выполнения."""
        graph = cli.parse_packages(SAMPLE_INDEX)
        with self.assertRaises(cli.PipelineError):
            cli.direct_dependencies(graph, "wget")


class MainTest(unittest.TestCase):
    """Коды завершения приложения."""

    def test_error_returns_config_exit_code(self):
        """Некорректный параметр даёт код завершения 2."""
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            code = cli.main(["Bad Name", "https://example.com/Packages.gz"])
        self.assertEqual(code, cli.EXIT_CONFIG_ERROR)
        self.assertIn("ошибка:", err.getvalue())


if __name__ == "__main__":
    unittest.main()

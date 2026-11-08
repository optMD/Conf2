"""Тесты прототипа CLI: конфигурация и проверка параметров."""

import contextlib
import io
import os
import tempfile
import unittest

import main as cli


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
            cli.load_config(
                ["A", "/no/such/file", "--mode", "test"]
            )

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
        with self.assertRaises(SystemExit):
            cli.load_config(
                ["curl", "https://example.com/Packages.gz",
                 "--direct", "--reverse"]
            )


class MainTest(unittest.TestCase):
    """Запуск приложения: вывод параметров и коды завершения."""

    def test_prints_key_value_settings(self):
        """Приложение печатает параметры в формате ключ-значение."""
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = cli.main(["curl", "https://example.com/Packages.gz"])
        self.assertEqual(code, 0)
        self.assertIn("package: curl", out.getvalue())
        self.assertIn("mode: repo", out.getvalue())

    def test_error_returns_config_exit_code(self):
        """Некорректный параметр даёт код завершения 2."""
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            code = cli.main(["Bad Name", "https://example.com/Packages.gz"])
        self.assertEqual(code, cli.EXIT_CONFIG_ERROR)
        self.assertIn("ошибка:", err.getvalue())


class TestGraphConfigTest(unittest.TestCase):
    """Успешный тестовый режим с существующим файлом."""

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


if __name__ == "__main__":
    unittest.main()

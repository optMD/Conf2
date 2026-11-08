"""Тесты обхода графа: BFS, глубина, циклы и тестовый режим."""

import os
import tempfile
import unittest

import main as cli

DATA_DIR = os.path.join(cli.ROOT, "tests", "data")


class TraverseTest(unittest.TestCase):
    """Обход в ширину на небольших графах."""

    def test_chain_reaches_every_node(self):
        """Цепочка A → B → C достигает всех узлов по порядку."""
        nodes, _ = cli.traverse({"A": ["B"], "B": ["C"]}, "A")
        self.assertEqual(nodes, ["A", "B", "C"])

    def test_cycle_terminates(self):
        """Цикл не приводит к бесконечному обходу."""
        graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
        nodes, edges = cli.traverse(graph, "A")
        self.assertEqual(sorted(nodes), ["A", "B", "C"])
        self.assertIn(("C", "A"), edges)

    def test_diamond_visits_shared_node_once(self):
        """Общий узел D попадает в результат один раз."""
        graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"]}
        nodes, _ = cli.traverse(graph, "A")
        self.assertEqual(nodes.count("D"), 1)

    def test_disconnected_part_is_not_reached(self):
        """Несвязанная компонента C → D не попадает в обход A."""
        nodes, _ = cli.traverse({"A": ["B"], "C": ["D"]}, "A")
        self.assertNotIn("C", nodes)

    def test_depth_limit_keeps_only_direct(self):
        """Ограничение глубины 1 даёт только прямых соседей корня."""
        graph = {"A": ["B"], "B": ["C"]}
        nodes, _ = cli.traverse(graph, "A", cli.DIRECT_DEPTH)
        self.assertEqual(nodes, ["A", "B"])


class TestGraphFileTest(unittest.TestCase):
    """Тестовый режим: граф из файла и его ошибки."""

    def write_graph(self, text):
        """Записывает текст во временный файл и возвращает путь."""
        fd, path = tempfile.mkstemp(suffix=".txt")
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        self.addCleanup(os.unlink, path)
        return path

    def test_loads_cycle_file(self):
        """Файл cycle.txt из tests/data читается в непустой граф."""
        graph = cli.load_test_graph(os.path.join(DATA_DIR, "cycle.txt"))
        self.assertTrue(graph)

    def test_lowercase_name_is_rejected(self):
        """Строчная буква в имени узла даёт ошибку."""
        with self.assertRaises(cli.PipelineError):
            cli.load_test_graph(self.write_graph("a: B\n"))

    def test_missing_colon_is_rejected(self):
        """Строка без двоеточия даёт ошибку."""
        with self.assertRaises(cli.PipelineError):
            cli.load_test_graph(self.write_graph("A B\n"))

    def test_empty_file_is_rejected(self):
        """Файл без узлов даёт ошибку."""
        with self.assertRaises(cli.PipelineError):
            cli.load_test_graph(self.write_graph("\n\n"))

    def test_transitive_and_direct_dependencies(self):
        """Без --direct выводятся все достижимые узлы, с --direct — только прямые."""
        path = self.write_graph("A: B\nB: C\n")
        full = cli.Config("A", path, cli.MODE_TEST, "g.png", False, False)
        direct = cli.Config("A", path, cli.MODE_TEST, "g.png", True, False)
        self.assertEqual(cli.find_dependencies(full), ["B", "C"])
        self.assertEqual(cli.find_dependencies(direct), ["B"])

    def test_unknown_package_is_an_error(self):
        """Пакета нет в тестовом графе — ошибка выполнения."""
        path = self.write_graph("A: B\n")
        config = cli.Config("Z", path, cli.MODE_TEST, "g.png", False, False)
        with self.assertRaises(cli.PipelineError):
            cli.find_dependencies(config)


if __name__ == "__main__":
    unittest.main()

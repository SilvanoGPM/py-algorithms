import unittest
from searchers.bfs import bfs, Graph

class TestBreadthFirstSearch(unittest.TestCase):
    def test_find_shortest_path(self):
        expected_first_path = [0, 3, 5, 1]
        expected_second_path = [0, 4]

        g = Graph(True)

        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        g.add_edge(1, 2)
        g.add_edge(1, 4)
        g.add_edge(2, 4)
        g.add_edge(3, 4)
        g.add_edge(3, 5)
        g.add_edge(4, 5)
        g.add_edge(5, 1)

        first_path = bfs(g, 0, 1)
        second_path = bfs(g, 0, 4)
        empty_path = bfs(g, 1, 0)

        self.assertListEqual(first_path, expected_first_path)
        self.assertListEqual(second_path, expected_second_path)
        self.assertListEqual(second_path, expected_second_path)
        self.assertListEqual(empty_path, [])

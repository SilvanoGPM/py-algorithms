import unittest
from searchers.dfs import dfs, Graph

class TestDepthFirstSearch(unittest.TestCase):
    def test_find_path(self):
        expected_first_path = [0, 3, 5, 1, 4]
        expected_second_path = [0, 2]
        
        g = Graph(True)

        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(1, 2)
        g.add_edge(1, 4)
        g.add_edge(2, 4)
        g.add_edge(3, 5)
        g.add_edge(4, 5)
        g.add_edge(5, 1)

        first_path = dfs(g, 0, 4)
        second_path = dfs(g, 0, 2)
        none_path = dfs(g, 1, 0)

        self.assertListEqual(first_path, expected_first_path)
        self.assertListEqual(second_path, expected_second_path)
        self.assertListEqual(none_path, [])
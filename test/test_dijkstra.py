import unittest

from searchers.dijkstra import dijkstra, Graph

class TestDijkstra(unittest.TestCase):
    def test_find_paths_with_less_costs(self):
        expected_paths = {1: {'from': 1, 'cost': 0}, 2: {'from': 1, 'cost': 4}, 3: {'from': 2, 'cost': 6}, 4: {'from': 2, 'cost': 5}}
        
        g = Graph()

        g.add_edge(1, 2, 4)
        g.add_edge(1, 3, 7)
        g.add_edge(1, 4, 6)
        g.add_edge(2, 3, 2)
        g.add_edge(2, 4, 1)
        g.add_edge(3, 4, 1)

        paths = dijkstra(g, 1)

        self.assertDictEqual(paths, expected_paths)
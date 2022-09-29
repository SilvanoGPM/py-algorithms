import unittest

from searchers.sequential_search import sequential_search

class SequentialSearchTest(unittest.TestCase):
    def test_search(self):
        expected_key = 2

        key_found = sequential_search([1, 2, 3], 3)

        self.assertEqual(key_found, expected_key)

    def test_search_not_found(self):
            expected_key = -1

            key_found = sequential_search([1, 2, 3], 4)

            self.assertEqual(key_found, expected_key)
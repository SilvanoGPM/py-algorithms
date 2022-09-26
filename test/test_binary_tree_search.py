import unittest

from searchers.binary_tree_search import SearchBinaryTree

class SearchBinaryTreeTest(unittest.TestCase):
    def test_search(self):
        expected_value = 10

        tree = SearchBinaryTree([20, 13, 3, 10, 14])

        value_found = tree.search(10)
        
        self.assertEqual(value_found.value, expected_value)


    def test_search_not_found(self):
        expected_value = None

        tree = SearchBinaryTree([20, 13, 3, 10, 14])

        value_found = tree.search(1000)
        
        self.assertEqual(value_found, expected_value)

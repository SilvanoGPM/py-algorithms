import unittest

from sorters.binary_tree_sort import SortBinaryTree

class SortBinaryTreeTest(unittest.TestCase):
    def test_sort_asc(self):
        array = [4, 1, 6, 7, 3, 2]
        expected_array = [1, 2, 3, 4, 6, 7]

        sorted_array = SortBinaryTree(array).sort()
        
        self.assertListEqual(sorted_array, expected_array)

    def test_sort_desc(self):
        array = [4, 1, 6, 7, 3, 2]
        expected_array = [7, 6, 4, 3, 2, 1]

        sorted_array = SortBinaryTree(array).sort(False)

        self.assertListEqual(sorted_array, expected_array)

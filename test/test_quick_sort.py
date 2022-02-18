import unittest

from sorters.quick_sort import quick_sort

class QuickSortTest(unittest.TestCase):
    def test_quick_sort_asc(self):
        array = [4, 1, 6, 7, 3, 2]
        expected_array = [1, 2, 3, 4, 6, 7]

        sorted_array = quick_sort(array)

        self.assertListEqual(sorted_array, expected_array)

    def test_merge_sort_desc(self):
            array = [4, 1, 6, 7, 3, 2]
            expected_array = [7, 6, 4, 3, 2, 1]

            sorted_array = quick_sort(array, asc=False)

            self.assertListEqual(sorted_array, expected_array)

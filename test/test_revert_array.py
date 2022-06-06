import unittest

from others.revert_array import revert_array


class RevertArrayTest(unittest.TestCase):
    def test_revert_array(self):
        array = [1, 5, 3, 7]
        expected_array = [7, 3, 5, 1]

        reverted_array = revert_array(array)

        self.assertListEqual(reverted_array, expected_array)

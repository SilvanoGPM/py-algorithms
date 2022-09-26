import unittest

from graphs.binary_tree import BinaryTree, Node


class BinaryTreeTest(unittest.TestCase):
    def test_node(self):
        expected_value = 10
        expected_left_value = 5
        expected_right_value = None

        node = Node(10, Node(5))

        self.assertEqual(node.value, expected_value)
        self.assertEqual(node.left.value, expected_left_value)
        self.assertEqual(node.right, expected_right_value)

    def test_binary_tree(self):
        expected_root_value = 8
        expected_root_left_value = 5
        expected_root_right_value = 12
        
        tree = BinaryTree()

        tree.insert(8)
        tree.insert(5)
        tree.insert(12)

        self.assertEqual(tree.root.value, expected_root_value)
        self.assertEqual(tree.root.left.value, expected_root_left_value)
        self.assertEqual(tree.root.right.value, expected_root_right_value)

    def test_binary_tree_with_iterable(self):
        expected_root_value = 'd'
        expected_root_left_value = 'a'
        expected_root_right_value = 'g'
        
        tree = BinaryTree('dag')

        self.assertEqual(tree.root.value, expected_root_value)
        self.assertEqual(tree.root.left.value, expected_root_left_value)
        self.assertEqual(tree.root.right.value, expected_root_right_value)
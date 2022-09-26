from graphs.binary_tree import BinaryTree, Node

class BinaryTreeSearch(BinaryTree):
    def search(self, value) -> Node:
        actual = self.root

        while True:
            if actual.value == value:
                return actual

            if value < actual.value:
                if not actual.left:
                    return None

                actual = actual.left
            else:
                if not actual.right:
                    return None

                actual = actual.right
            
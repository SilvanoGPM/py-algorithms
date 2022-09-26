class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value} -> [{self.left}, {self.right}]'


class BinaryTree:
    def __init__(self, iterable = []):
        self.root = None

        [self.insert(i) for i in iterable]

    def insert(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        actual = self.root

        while True:
            if value < actual.value:
                if not actual.left:
                    actual.left = node
                    break

                actual = actual.left
            else:
                if not actual.right:
                    actual.right = node
                    break

                actual = actual.right

    def __str__(self):
        return str(self.root)

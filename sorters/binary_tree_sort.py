from graphs.binary_tree import BinaryTree, Node


class SortBinaryTree(BinaryTree):
    def sort_symetric_desc(self, node: Node, elements = []):
        if node:
            self.sort_symetric_desc(node.right)
            elements.append(node.value)
            self.sort_symetric_desc(node.left)
    
        return elements
    
    def sort_symetric_asc(self, node: Node, elements = []):
        if node:
            self.sort_symetric_asc(node.left)
            elements.append(node.value)
            self.sort_symetric_asc(node.right)
    
        return elements

    def sort(self, asc = True):
        if asc:
            return self.sort_symetric_asc(self.root)

        return self.sort_symetric_desc(self.root)

import sys
sys.path.append('../trees')  # Add the correct path to the sys.path list
from node import Node  # Import the 'Node' class from the correct package

class Tree:
    def __init__(self):
        self.root = None

    def binary_search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        if root.data < key:
            return self.binary_search(root.right, key)
        return self.binary_search(root.left, key)

# Tree structure
#           9
#         /   \
#        3     12
#       / \   / \
#      1   4 10  17
#     / \      \   \
#    0   2     11   19
#
if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(9)
    tree.root.left = Node(3)
    tree.root.right = Node(12)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(17)
    tree.root.left.left.left = Node(0)
    tree.root.left.left.right = Node(2)
    tree.root.right.left.right = Node(11)
    tree.root.right.right.right = Node(19)
    print("search for 17 ", tree.binary_search(tree.root, 17)) # True
    print("search for 10", tree.binary_search(tree.root, 10)) # True
    print("search for 1 ", tree.binary_search(tree.root, 1)) # True
    print("search for 9 ", tree.binary_search(tree.root, 9)) # True
    print("search for 8 ", tree.binary_search(tree.root, 8)) # False
    print("search for 6 ", tree.binary_search(tree.root, 6)) # False
    print("search for 12 ", tree.binary_search(tree.root, 12)) # True


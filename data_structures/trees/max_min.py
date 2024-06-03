#  GFG: https://www.geeksforgeeks.org/problems/max-and-min-element-in-binary-tree/
# Given a Binary Tree, find maximum and minimum elements in it.
import sys
sys.path.append('../trees')  # Add the correct path to the sys.path list
from node import Node  # Import the 'Node' class from the correct package

class Tree:
    def findMax(self,root):
        maximum = -1
        def max_tree(root):
            nonlocal maximum
            if(root is None):
                return
            maximum = max(root.data, maximum)
            max_tree(root.left)
            max_tree(root.right)
        max_tree(root)
        return maximum
        #code here
    def findMin(self,root):
        minimum = 1000000
        def min_tree(root):
            nonlocal minimum
            if(root is None):
                return
            minimum = min(root.data, minimum)
            min_tree(root.left)
            min_tree(root.right)
        min_tree(root)
        return minimum


#           1
#         /   \
#        2     3
#       / \   / \
#      4   5 6   7
#     / \
#    8   9
#
#  Consider the above tree, max = 9, min = 1

if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.left.left = Node(8)
    tree.root.left.left.right = Node(9)
    print(tree.findMax(tree.root)) # 9
    print(tree.findMin(tree.root)) # 1
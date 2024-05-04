# Tree traversal
import sys
sys.path.append('../trees')
from node import Node

class Tree2:
    def __init__ (self):
        self.root = None

    # recursion left ->  root -> right
    def inorderTraversalRecursion(self,root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data, end=' ')
            self. inorderTraversal(root.right)

    # iteration
    def inorderTraversalIteration(self,root):
        stack = []
        result = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            # If the stack is empty, break the loop
            if not stack:
                break
            root = stack.pop()
            result.append(root.data)
            root = root.right
        return result

    # recursion root -> left -> right
    def preOrderRecursion(self, root):
        if root:
            print(root.data)
            self.preOrderRecursion(root.left)
            self.preOrderRecursion(root.right)

    # Iteration root -> left -> right
    def preOrderIteration(self, root):
        stack = []
        result = []
        while(True):
            while(root):
                stack.append(root)
                result.append(root.data)
                root = root.left
            if(not stack):
                break
            root = stack.pop()
            root = root.right
        return result

    # Recursion left -> right -> root
    def postOrderRecurstion(self, root):
        if(root):
            self.postOrderRecurstion(root.left)
            self.postOrderRecurstion(root.right)
            print(root.data)

    # Iteration left -> right -> root
    def postOrderIteration(self, root):
        stack = []
        result = []
        stack.append(root)
        while(stack):
            root = stack.pop()
            result.append(root.data)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return result[::-1]
#           1
#         /   \
#        2     3
#       / \   / \
#      4   5 6   7
#     / \
#    8   9
#
#  Consider the above tree, the height of the tree is 4.
# Inorder: 8 4 9 2 5 1 6 3 7
# Preorder: 1 2 4 8 9 5 3 6 7
# Postorder: 8 9 4 5 2 6 7 3 1
if __name__ == '__main__':
    tree = Tree2()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.left.left = Node(8)
    tree.root.left.left.right = Node(9)
    # print("Inorder:", tree.inorderTraversalIteration(tree.root)) # 8 4 9 2 5 1 6 3 7
    print("PreOrder:", tree.preOrderIteration(tree.root)) # 1 2 4 8 9 5 3 6 7
    # print("PostOrder:", tree.postOrderIteration(tree.root)) # 8 9 4 5 2 6 7 3 1


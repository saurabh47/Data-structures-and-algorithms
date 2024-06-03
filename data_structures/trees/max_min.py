#  GFG: https://www.geeksforgeeks.org/problems/max-and-min-element-in-binary-tree/
# Given a Binary Tree, find maximum and minimum elements in it.
class Solution:
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
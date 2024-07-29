### Problem 1022. Sum of Root To Leaf Binary Numbers (Easy): https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

### Tags: Tree, Depth First Search, Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def path(root, total):
            if(root is None):
                return 0
            if(root.left is None and root.right is None):
                return total*2 + root.val
            left = path(root.left, total*2 + root.val)
            right = path(root.right, total*2 + root.val)
            return left + right
        return path(root, 0)

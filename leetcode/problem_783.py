### Problem 783. Minimum Distance Between BST Nodes
### Tags: Tree, Depth First Search, Binary Search Tree

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = []
        stack = []
        while(True):
            while(root):
                stack.append(root)
                root = root.left
            if(not stack):
                break
            root = stack.pop()
            result.append(root.val)
            root = root.right
        min_val = 100000
        for i in range(1, len(result)):
            curr = result[i]
            prev = result[i - 1]
            if(abs(curr - prev) < min_val):
                min_val = abs(curr - prev)
        return min_val

# recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev ,min_val = None, 100000
        def min_diff(root):
            if(root is None):
                return 
            min_diff(root.left)
            nonlocal prev, min_val
            if(prev):
                min_val = min((root.val - prev.val), min_val)
            prev = root
            min_diff(root.right)
        min_diff(root)
        return min_val
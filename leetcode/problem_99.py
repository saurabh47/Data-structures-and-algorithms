### Problem 99. Recover Binary Search Tree (Hard): https://leetcode.com/problems/recover-binary-search-tree/

### Tags: Tree, Depth First Search, Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev = None
        first = None
        end = None
        def recover(root):
            if(root is None):
                return 
            recover(root.left)
            nonlocal prev, first, end
            if(prev):
                if(prev.val > root.val):
                    if(first is None):
                        first = prev
                    end = root
            prev = root
            recover(root.right)
        recover(root)
        temp = first.val
        first.val = end.val
        end.val = temp

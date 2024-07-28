### Problem 236: Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
### Tags: [Tree]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root is None):
            return None
        elif(root.val == p.val or root.val == q.val):
            return root

        found_left = self.lowestCommonAncestor(root.left, p, q)
        found_right = self.lowestCommonAncestor(root.right, p, q)

        if(found_left and found_right):
            return root
        elif(found_left and not found_right):
            return found_left
        elif(not found_left and found_right):
            return found_right
        else:
            return None
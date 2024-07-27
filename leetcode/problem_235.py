### Problem 235. Lowest Common Ancestor of a Binary Search Tree (Easy): https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

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
        if(root.val == p.val and root.val == q.val):
            return root
        elif(root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif(root.val < p.val and root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


# Iterative
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while(root):
            if(root.val == p.val and root.val == q.val):
                return root
            elif(root.val > p.val and root.val > q.val):
                root = root.left
            elif(root.val < p.val and root.val < q.val):
                root = root.right
            else:
                return root
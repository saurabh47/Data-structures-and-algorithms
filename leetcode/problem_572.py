### Problem 572. Subtree of Another Tree (Easy): https://leetcode.com/problems/subtree-of-another-tree/

### Tags: Tree, Recursion, DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        top = root
        while(True):
            while(top):
                stack.append(top)
                top = top.left
            if(not stack):
                return False
            top = stack.pop()
            if(top.val == subRoot.val):
                if(self.isSame(top, subRoot)):
                    return True
            top = top.right
        return False


    def isSame(self, root1: TreeNode, root2: TreeNode) -> bool:
        if((root1 and not root2) or (not root1 and root2)):
            return False
        elif(not root1 and not root2):
            return True
        elif(root1.val != root2.val):
            return False
        else:
            return  (self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right))
### Problem 98: Validate Binary Search Tree
###

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### Iterative Solution
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = self.inOrder(root)
        for i in range(1, len(inorder)):
            prev = inorder[i - 1]
            curr = inorder[i]
            if(prev >= curr):
                return False
        return True

    def inOrder(self, root):
        stack = []
        result = []
        while(True):
            while(root):
                stack.append(root)
                root = root.left
            if(not stack):
                break
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
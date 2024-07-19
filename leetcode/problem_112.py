### Problem 112. Path Sum
### Tags: Tree, Depth First Search, Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPath(root,targetSum):
            if(root is None):
                return False
            else:
                targetSum -= root.val
                if(root.left is None and root.right is None):
                    return targetSum == 0
                return hasPath(root.left, targetSum) or hasPath(root.right, targetSum)
        return hasPath(root, targetSum)
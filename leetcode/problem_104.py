### Problem 104: Maximum Depth of Binary Tree (Easy): https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return max(lh, rh) + 1
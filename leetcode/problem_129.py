### Problem 129. Sum Root to Leaf Numbers (Medium): https://leetcode.com/problems/sum-root-to-leaf-numbers/

### Tags: Tree, Depth First Search, Recursion
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def path(root, sum_n):
            if(root is None):
                return 0
            if(root.left is None and root.right is None):
                return sum_n*10 + root.val
            left = path(root.left, sum_n*10 + root.val)
            right = path(root.right, sum_n*10 + root.val)
            return left + right
        return path(root, 0)
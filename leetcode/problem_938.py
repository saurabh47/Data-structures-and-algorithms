### Problem 938. Range Sum of BST (Easy) 
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        stack = []
        start = root
        while(True):
            while(start):
                stack.append(start)
                start = start.left
            if(not stack):
                break
            start = stack.pop()
            if(start.val >= low and start.val <= high):
                result +=start.val
            start = start.right
        return result

### Recursive Solution
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rangeSum(r):
            if(r is None):
                return 0
            val = 0
            if(r.val >= low and r.val <= high):
                val = r.val
            return rangeSum(r.left) + val + rangeSum(r.right)
        return rangeSum(root)

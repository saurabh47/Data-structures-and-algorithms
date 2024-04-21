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

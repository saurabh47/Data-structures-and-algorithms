### Problem 513. Find Bottom Left Tree Value (Medium): https://leetcode.com/problems/find-bottom-left-tree-value/

from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        leftMost = root.val
        while(True):
            size = len(q)
            if(size == 0):
                return leftMost
            first = True
            while(size > 0):
                top = q.popleft()
                if(first):
                    leftMost = top.val
                    first = not first
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)
                size -=1
        return leftMost
    
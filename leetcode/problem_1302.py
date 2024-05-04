### Problem 1302. Deepest Leaves Sum (Medium): https://leetcode.com/problems/deepest-leaves-sum/
 
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        deep_sum = 0
        if(root is None):
            return deep_sum
        q.append(root)
        while(True):
            size = len(q)
            if(size == 0):
                return deep_sum
            deep_sum = 0
            while(size > 0):
                front = q.popleft()
                deep_sum += front.val
                if(front.left):
                    q.append(front.left)
                if(front.right):
                    q.append(front.right)
                size -= 1
        return deep_sum
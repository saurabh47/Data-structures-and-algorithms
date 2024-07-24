### Problem 515. Find Largest Value in Each Tree Row (Medium)
'''
    You need to find the largest value in each row of a binary tree.
    Example 1:
    Input:
            1
           / \
          3   2
         / \   \
        5   3   9
    Output: [1, 3, 9]
'''

### Tags: Binary Tree, BFS, Queue
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        if(root is None):
            return result
        q.append(root)
        while(True):
            size = len(q)
            if(size == 0):
                break
            maximum = -pow(2,31)
            while(size > 0):
                top = q.popleft()
                maximum = max(top.val, maximum)
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)
                size -=1
            result.append(maximum)
        return result
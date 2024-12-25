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

# DFS:
# # Time Complexity: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # run dfs
        # for first element at each level add to result
        # for rest update the element by maxvalue at that level (index in result)
        result = []
        def dfs(r, depth):
            if(r is None):
                return 
            if(depth >= len(result)):
                result.append(r.val)
            else:
                result[depth] = max(result[depth], r.val)
            dfs(r.left, depth + 1)
            dfs(r.right, depth + 1)

        dfs(root, 0)
        return result
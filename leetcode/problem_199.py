### Problem 199. Binary Tree Right Side View (Medium): https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        result = []
        if(root is None):
            return result
        q.append(root)
        while(True):
            size = len(q)
            if(size == 0):
                return result
            rv = 0
            while(size > 0):
                top = q.popleft()
                rv = top.val
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)
                size -= 1
            result.append(rv)
        return result
### Problem 103. Binary Tree Zigzag Level Order Traversal (Medium): https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque()
        if(root is None):
            return result
        q.append(root)
        alternate = False
        while(True):
            zig_zag = []
            size = len(q)
            if(size == 0):
                return result
            while(size > 0):
                top = q.popleft()
                zig_zag.append(top.val)
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)
                size -= 1
            if(alternate):
                result.append(reversed(zig_zag))
            else:
                result.append(reversedzig_zag)
            alternate = not alternate
        return result

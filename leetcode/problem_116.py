### Problem 116. Populating Next Right Pointers in Each Node
### Tags: Tree, BFS

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        result = []
        if(root is None):
            return None
        q.append(root)
        while(True):
            size = len(q)
            if(size == 0):
                break
            levels = []
            while(size > 0):
                top = Node()
                if(size > 1):
                    top = q.popleft()
                    nextAddr = q[0]
                    top.next = nextAddr
                else:
                    top = q.popleft()
                levels.append(top)
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)
                size -=1
            result.append(levels)
        return root
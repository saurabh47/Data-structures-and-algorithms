#### Problem 1609. Even Odd Tree (Medium)
### tags: binary tree, BFS, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        #  do a BFS traversal
        #  at any point if this conditions is satisfied return False
        #   - at even level -> even number
        #   - at a odd level -> odd
        #   - if any level is not sorted
        #  otherwise continue traversing

        q = deque()
        level = 0
        result = True
        if(root is None):
            return True
        q.append(root)
        while(True):
            size = len(q)
            prev = -1
            while(size > 0):
                top = q.popleft()
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)   
                size -= 1
                if((level % 2 == 0 and top.val % 2 == 0)
                    or (level % 2 != 0 and top.val % 2 != 0)):
                    result = False
                    return result
                if(prev != -1):
                    if((level % 2 == 0 and prev >= top.val) or
                    (level % 2 != 0 and prev <= top.val)):
                        return False
                prev = top.val
            level += 1
            if(len(q) == 0):
                break
        return result
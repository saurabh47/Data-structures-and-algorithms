### Problem 2415. Reverse Odd Level Nodes in Binary Tree (Medium): https://leetcode.com/problems/reverse-odd-level-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        
        def swap(i, j):
            t = q[i].val
            q[i].val = q[j].val
            q[j].val = t

        q.append(root)
        count = 0
        while(True):
            size = len(q)
            if(size == 0):
                break
            if(count & 1 == 1):
                l, r = 0, len(q) - 1
                while(l < r):
                    swap(l , r)
                    l += 1
                    r -= 1
            while(size > 0):
                top = q.popleft()
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)
                size -= 1
            count += 1
        return root

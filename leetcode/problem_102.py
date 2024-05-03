### Problem 102. 
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []
        q.append(root)
        if(root is None):
            return result
        while(True):
            size = len(q)
            if(size == 0):
                return result
            data = []
            while(size > 0):
                temp = q.popleft()
                data.append(temp.val)
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
                size -=1 
            result.append(data)
        return result
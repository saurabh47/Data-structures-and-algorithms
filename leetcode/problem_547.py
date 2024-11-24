### Problem 547. Number of Provinces (Medium): https://leetcode.com/problems/number-of-provinces/
### tags: Graph, Connected Components, Depth First Search, Breadth First Search

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = {}
        n = len(isConnected)
        visited = set()
        count = 0
        for conn in range(n):
            if(conn in visited):
                continue
            count += 1
            q = deque()
            q.append(conn)
            visited.add(conn)
            while(len(q) != 0):
                top = q.popleft()
                neighbors = isConnected[top]
                for i in range(n):
                    if(neighbors[i] == 1 and i not in visited):
                        q.append(i)
                        visited.add(i)
            # print("visited from i=", conn ," =", visited)
        return count
            

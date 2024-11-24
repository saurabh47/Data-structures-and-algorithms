### Problem 1971. Find if Path Exists in Graph (Easy): https://leetcode.com/problems/find-if-path-exists-in-graph/
### tags: Graph, BFS, Connected Components

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {}
        result = False
        for src, dst in edges:
            if(src in adj):
                adj[src].append(dst)
            else:
                adj[src] = [dst]
            if(dst in adj):
                adj[dst].append(src)
            else:
                adj[dst] = [src]
        
        visited = set()
        visited.add(source)
        q = deque()
        q.append(source)
        while(len(q) != 0):
            top = q.popleft()
            if(top in adj):
                neighbors = adj[top]
                for n in neighbors:
                    if(n not in visited):
                        q.append(n)
                        visited.add(n)
        return destination in visited
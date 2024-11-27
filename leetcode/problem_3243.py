### Problem 3243. Shortest Distance to Target Color
### tags: graph, bfs

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = {}
        def shortest_distance(source):
            q = deque()
            q.append((source, 0))
            distance = 0
            visited = set()
            visited.add(0)
            while(len(q) != 0):
                t, dist = q.popleft()
                if(t == n - 1):
                    return dist
                for neighbor in adj[t]:
                    if(neighbor not in visited):
                        q.append((neighbor, dist + 1))
                        visited.add(neighbor)

        for i in range(n - 1):
            adj[i] = [i + 1]
        adj[n-1] = []
        result = []
        for src, dest in queries:
            adj[src].append(dest)
            result.append(shortest_distance(0))
        return result
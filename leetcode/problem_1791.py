### Problem 1791. Find Center of Star Graph (Medium)
### tags: Graph, Degree, Hash Table
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        deg = defaultdict(int)
        for src, dest in edges:
            deg[src]+=1
            deg[dest]+=1
        return max(deg, key=deg.get)


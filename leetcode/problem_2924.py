### Problem 2924. Find the Champion (Medium): https://leetcode.com/problems/find-the-champion/
### tags: graph

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = defaultdict(int)
        for src, dest in edges:
            if(src not in incoming):
                incoming[src] = 0
            incoming[dest] += 1
        for i in range(n):
            if(i not in incoming):
                incoming[i] = 0

        count = 0
        champions = []
        for k , v in incoming.items():
            if(v == 0):
                champions.append(k)
        if(len(champions) > 1):
            return -1
        elif(len(champions) == 0):
            if(n > 1):
                return -1
            else:
                return n - 1
        return champions[0]

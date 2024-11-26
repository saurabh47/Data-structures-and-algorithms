### Problem 2924. Find the Champion (Medium): https://leetcode.com/problems/find-the-champion/
### tags: graph

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = {}
        for i in range(n):
            incoming[i] = 0
        
        for src, dest in edges:
            incoming[dest] += 1

        count = 0
        champions = []
        for k , v in incoming.items():
            if(v == 0):
                champions.append(k)
        if(len(champions) > 1):
            return -1
        return champions[0]

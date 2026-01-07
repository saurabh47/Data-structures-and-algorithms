### Problem 3208. Number of Alternating Groups (Medium) 
### tags: array, sliding window
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count = 0
        start = 0 
        n = len(colors)
        for end in range(1, n + k - 1):
            if(colors[end % n] == colors[(end - 1) % n]):
                start = end
            if(end - start + 1 > k):
                start += 1
            if(end - start + 1 == k):
                count += 1
        return count
        
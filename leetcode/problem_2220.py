### Problem 2220. Minimum Bit Flips to Convert Number
### tags: bit manipulation
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # 100011
        # 010110
        # 110101 (XOR)
        mask = 1
        count = 0
        t = start ^ goal
        while(t > 0):
            if(t & 1):
                count += 1
            t >>= 1
        return count
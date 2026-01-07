### Problem 2379. Minimum Number of Recoloring (Medium): https://leetcode.com/problems/minimum-number-of-recoloring/

### tags: Sliding Window, Two Pointers
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # find index with max whites
        whites = 0
        start = 0
        res = k
        for end in range(len(blocks)):
            win_len = end - start + 1
            if(blocks[end] == 'W'):
                whites += 1
            if(win_len == k):
                res = min(res, whites)
                if(blocks[start] == 'W'):
                    whites -= 1
                start += 1
        return res
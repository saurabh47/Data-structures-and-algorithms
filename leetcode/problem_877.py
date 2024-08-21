### Problem 877. Stone Game (Medium): https://leetcode.com/problems/stone-game/
### tags: dynamic programming
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        def dfs(start, end):
            if(start > end):
                return 0
            if((start, end) in cache):
                return cache[(start, end)]
            bobs_turn = True if (end - start) % 2 != 0 else False
            left, right = 0, 0
            if(not bobs_turn):
                left = piles[start]
                right = piles[end]
            # alice can choose either of the choice
            res1 = dfs(start + 1, end) + left
            res2 = dfs(start, end - 1) + right

            cache[(start, end)] = max(res1, res2)
            return cache[(start, end)]
        return dfs(0, len(piles) - 1)
### Problem 39. Combination Sum (Medium): https://leetcode.com/problems/combination-sum/
### tags: backtracking, recursion
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(index, total, arr):
            if(index >= len(candidates) or total > target):
                return
            if(total == target):
                result.append(arr.copy())
                return

            arr.append(candidates[index])
            dfs(index, total + candidates[index], arr)
            arr.pop()
            dfs(index + 1, total, arr)

        dfs(0, 0, [])
        return result
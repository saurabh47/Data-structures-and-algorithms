### Problem 40. Combination Sum II (Medium): https://leetcode.com/problems/combination-sum-ii/
### tags: backtracking, recursion

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(total, arr, index):
            if(total == target):
                result.append(arr.copy())
                return
            if(index >= len(candidates) or total > target):
                return
            arr.append(candidates[index])
            dfs(total + candidates[index], arr, index + 1)
            arr.pop()
            while(index + 1 < len(candidates) and (candidates[index + 1] == candidates[index])):
                index += 1
            dfs(total, arr, index + 1)


        dfs(0, [], 0)
        return result
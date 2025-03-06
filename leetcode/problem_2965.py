### Problem 2965. Find Missing and Repeated Values (Easy): https://leetcode.com/problems/find-missing-and-repeated-values/
### tags: array, set, math

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        dup = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] in s):
                    dup = grid[i][j]
                else:
                    s.add(grid[i][j])
        missing = -1
        for i in range(1, len(s) + 2):
            if(i not in s):
                missing = i
                break
        return [dup, missing]

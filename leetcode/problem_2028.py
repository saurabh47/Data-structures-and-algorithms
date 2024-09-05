### Problem 2028. Find missing observations
### tags: array, math, simulation
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumX = (mean) * (len(rolls) + n) - sum(rolls)
        result = []
        if(sumX < n or sumX > (6 * n)):
            return []
        while(n):
            numX = min(6, sumX - n + 1)
            result.append(numX)
            sumX -= numX
            n -= 1
        return result
        
### Problem 2579. Colored Cells in a Grid
### tags: math
class Solution:
    def coloredCells(self, n: int) -> int:
        
        # f(1) => 1
        # f(2) => f(1) + 4 => 1 + 4 = 5
        # f(3) => f(2) + 4 * 2 = 13
        # f(4) => f(3) + 4 * 3 = 13 + 12 = 25
        # f(5) => f(4) + 4 * 4 = 25 + 16 = 41
        # f(6) => f(5) + 4 * 5 = 41 + 20 = 61
        if(n == 1):
            return 1
        return self.coloredCells(n - 1) + 4 * (n - 1)

# Optimized

class Solution2:
    def coloredCells(self, n: int) -> int:
        
        # f(1) => 1
        # f(2) => f(1) + 4 => 1 + 4 = 5
        # f(3) => f(2) + 4 * 2 = 13
        # f(4) => f(3) + 4 * 3 = 13 + 12 = 25
        # f(5) => f(4) + 4 * 4 = 25 + 16 = 41
        # f(6) => f(5) + 4 * 5 = 41 + 20 = 61
        result = 1
        prev = 1
        if(n == 1):
            return result
        for i in range(2, n+1):
            result = prev + 4 * (i - 1)
            prev = result
        return result
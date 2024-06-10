### Problem 1051. Height Checker (Easy)
### Tags: [Array, Sorting]

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(expected)):
            if(expected[i] != heights[i]):
                count += 1
        return count
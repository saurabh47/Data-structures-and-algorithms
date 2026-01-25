# Problem 11: Container With Most Water (Medium): https://leetcode.com/problems/container-with-most-water/

from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Approach

        # Given
        # - Array: Heights of bars at i

        # Goal
        # - find maximum container area
        # - find two largest bars at longest distance apart
        # - area = min(bar1, bar2) * dist(bar1, bar2)
        # - compare the area with largest we currently have
        # - return the largest

        start = 0
        end = len(height) - 1
        max_water = 0
        while(start < end):
            h = min(height[start], height[end])
            width = end - start
            area = h * width
            max_water = max(area, max_water)
            if(height[start] < height[end]):
                start += 1
            else:
                end -= 1
        return max_water


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7])) # 49
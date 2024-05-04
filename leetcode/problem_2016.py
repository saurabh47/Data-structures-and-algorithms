### Problem 2016. Maximum Difference Between Increasing Elements (Easy)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        start = 0
        end = start
        max_diff = 0
        while(end < len(nums)):
            diff = nums[end] - nums[start]
            if(nums[end] < nums[start]):
                start = end
            if(nums[end] - nums[start] > max_diff):
                max_diff = diff
            end += 1
        if(max_diff == 0):
            return -1
        else:
            return max_diff

### Problem 1800. Maximum Ascending Subarray Sum
### tags: array
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_s = 0
        curr_s = 0
        prev = 0
        for end in range(len(nums)):
            if(nums[end] <= prev):
                curr_s = nums[end]
            else:
                curr_s += nums[end]
            prev = nums[end]
            max_s = max(max_s, curr_s)
        return max_s
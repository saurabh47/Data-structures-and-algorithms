### Problem 414. Third Maximum Number (Easy): https://leetcode.com/problems/third-maximum-number/
### tags: array, sorting
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        index = 0
        for i in range(len(nums) - 1, 0, -1):
            if(nums[i] != nums[i - 1]):
                index += 1
            if(index == 2):
                return nums[i - 1]
        return nums[-1]
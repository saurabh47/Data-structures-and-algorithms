### Problem 16: 3Sum Closest (Medium): https://leetcode.com/problems/3sum-closest/
# Tags: Array, Two Pointers
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        nums.sort()
        sum3 = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums) -1
            while(start < end):
                s = nums[i] + nums[start] + nums[end]
                if(abs(target-sum3) > abs(target - s)):
                    sum3 = s
                if(s > target):
                    end -= 1
                else:
                    start += 1
        return sum3
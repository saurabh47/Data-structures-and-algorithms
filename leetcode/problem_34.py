### Problem 34. Find First and Last Position of Element in Sorted Array (Medium): https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if(len(nums) == 0 or target < nums[0] or target > nums[-1]):
            return result
        i = 0
        while(nums[i] != target and i < len(nums)):
            if(nums[i] > target):
                return [-1, -1] 
            i+=1
        result[0] = i
        i = len(nums) - 1
        while(nums[i] != target and i > result[0]):
            i -= 1
        result[1] = i
        return result


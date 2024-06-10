### Problem: Given an unsorted integer array, find the smallest missing positive integer.

### Tags: [Array, Hash Table]
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
            if(smallest in h):
                smallest += 1
        while(smallest in h):
            smallest += 1
        return smallest
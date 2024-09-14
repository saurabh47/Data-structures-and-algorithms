### problem 2419. Longest Subarray With Maximum Bitwise AND
### tags: array, bit manipulation

# hint: AND with smaller number will always be smaller than the smallest
# AND with a number iteself, is the number iteself
# We should find consecutive max number in the array to get max AND of subarray
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        res = 0
        max_fr = 0
        for num in nums:
            if(num == max_and):
                res += 1
            else:
                res = 0
            max_fr = max(res, max_fr)
        return max_fr
    

### Optimized

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        size = 0
        curr_max = 0
        for num in nums:
            if(num > curr_max):
                curr_max = num
                size = 1
                res = 0
            elif(num == curr_max):
                size += 1
            else:
                size = 0
            res = max(size, res)
        return res
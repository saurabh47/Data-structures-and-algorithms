### Problem 485. Max Consecutive Ones (Easy): https://leetcode.com/problems/max-consecutive-ones/
### tags: Array, Two Pointers
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        result = 0
        for end in range(len(nums)):
            if(nums[end] == 0):
                while(end < len(nums) and nums[end] == 0):
                    end += 1
                start = end
            else:
                win_len = end - start + 1
                result = max(win_len, result)
        return result

### Optimized Solution

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                count += 1
            else:
                count = 0
            result = max(count, result)
        return result
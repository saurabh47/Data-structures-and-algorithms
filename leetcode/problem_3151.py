### Problem 3151. Check if Array Is Special
### Tags: Array

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            x = nums[i-1]
            y = nums[i]
            # check if different parity
            if((x ^ y) & 1 == 0):
                return False
        return True
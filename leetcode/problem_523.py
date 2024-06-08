### Problem 523. Continuous Subarray Sum (Medium): https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rems = {0: -1}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            rem = s % k
            # we found a sub array multiple of k
            if(rem in rems):
                # check if subarray length >1
                if(i - rems[rem] > 1):
                    return True
            else:
                rems[rem] = i
        return False 


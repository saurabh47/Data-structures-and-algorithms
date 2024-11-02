### Problem 523. Continuous Subarray Sum (Medium): https://leetcode.com/problems/continuous-subarray-sum/

### Tags: Math, Array, Hash Table
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

# hint: store Prefix Sum % k in hashmap
# if we encounter same mod again that me found a subarray with sum%k==0
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lookUp = {}
        s = 0
        for i, num in enumerate(nums):
            s += num
            if(s % k== 0 and i > 0):
                return True
            if((s % k) in lookUp):
                if(abs(lookUp[s%k] - i) >= 2):
                    return True
            else:
                lookUp[s % k] = i
        return False


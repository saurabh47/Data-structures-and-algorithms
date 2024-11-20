### Problem 2395. Find Subarrays with Equal Sum (Medium)
### tags: Array, Hash table

# Time complexity: O(n^2)
# Memory complexity: O(1)
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums) - 1):
                if(nums[i] + nums[i + 1] == nums[j] + nums[j + 1]):
                    return True
        return False

# Time complexity: O(n)
# Memory complexity: O(n)
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        lookUp = {}
        for i in range(1, len(nums)):
            s = nums[i] + nums[i - 1]
            if(s in lookUp):
                return True
            else:
                lookUp[s] = i - 1
        return False
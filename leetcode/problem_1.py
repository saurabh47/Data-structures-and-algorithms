# Problem 1: Two Sum (Easy): https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff not in diffMap):
                diffMap[nums[i]] = i
            else:
                return [i, diffMap[diff]]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums,target)) # [0,1]
# Problem 1: Two Sum (Easy): https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums):
        map = {}
        for i in range(len(nums)):
            result = []
            difference = target - nums[i]
            if(difference in map):
                result.append(map[difference])
                result.append(i)
                return result;
            map[nums[i]] = i
        return [] 

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums,target)) # [0,1]
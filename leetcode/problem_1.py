# Problem 1: Two Sum (Easy): https://leetcode.com/problems/two-sum/

# Time Complexity O(n) memory: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff not in diffMap):
                diffMap[nums[i]] = i
            else:
                return [i, diffMap[diff]]

# Time Complexity O(nlogn) memory: O(1)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        print(nums)
        start = 0
        end = len(nums) - 1
        while(start < end):
            if(nums[start] + nums[end] == target):
                return [start, end]
            elif(nums[start] + nums[end] < target):
                start += 1
            else:
                end -= 1
        return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums,target)) # [0,1]
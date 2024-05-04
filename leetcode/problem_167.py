### Problem 167: Two Sum II - Input array is sorted (Easy): https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffMap = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if(diff not in diffMap):
                diffMap[numbers[i]] = i+1
            else:
                return [diffMap[diff], i+1]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums,target)) # [1,2]
    nums = [2,3,4]
    target = 6
    print(Solution().twoSum(nums,target)) # [1,3]
    nums = [-1,0]
    target = -1
    print(Solution().twoSum(nums,target)) # [1,2]
    nums = [1,2,3,4,4,9,56,90]
    target = 8
    print(Solution().twoSum(nums,target)) # [3,5]
    nums = [1,2,3,4,4,9,56,90]
    target = 10
    print(Solution().twoSum(nums,target)) # [3,6]
    nums = [1,2,3,4,4,9,56,90]
    target = 100
    print(Solution().twoSum(nums,target)) # [7,8]
    nums = [1,2,3,4,4,9,56,90]
    target = 65
    print(Solution().twoSum(nums,target)) # [6,7]
    nums = [1,2,3,4,4,9,56,90]
    target = 5
    print(Solution().twoSum(nums,target)) # [1,4]
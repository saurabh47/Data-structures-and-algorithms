### Problem 1480. Running Sum of 1d Array (Easy)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums

# Recursive solution
class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = self.sum_i(len(nums) - 1, nums)
        return result

    def sum_i(self, i:int, nums: List[int])-> List[int]:
        if(i < 1):
            return nums
        else:
            nums = self.sum_i(i-1, nums)
            nums[i] += nums[i-1]
            return nums

if __name__ == '__main__':
    s = Solution()
    print(s.runningSum([1,2,3,4])) # [1,3,6,10]
    print(s.runningSum([1,1,1,1,1])) # [1,2,3,4,5]
    print(s.runningSum([3,1,2,10,1])) # [3,4,6,16,17]
    print(s.runningSum([3,1,2,10,1,1])) # [3,4,6,16,17,18]
# Problem 525. Contiguous Array (Medium): https://leetcode.com/problems/contiguous-array/
# hint: Locations where the number of zeros and ones are the same are the same length of contiguous array.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        maxLength = 0
        # -1 -2 -1, -2, -3, -4, -3, -2
        # [0, 0, 1, 0, 0, 0, 1, 1]
        arr = {0:-1}
        for i in range(len(nums)):
            if(nums[i] == 1):
                count+=1
            else:
                count -= 1
            if(count in arr):
                maxLength = max(maxLength,i - arr[count])
            else:
                arr[count] = i
        return maxLength

if __name__ == "__main__":
    nums = [0,1,0,0,0,0,1,1]
    print(Solution().findMaxLength(nums)) # 6
    nums = [0,1,0,1]
    print(Solution().findMaxLength(nums)) # 4
    nums = [0,0,1,0,0,0,1,1]
    print(Solution().findMaxLength(nums)) # 6
    nums = [0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0 ]
    print(Solution().findMaxLength(nums)) # 14

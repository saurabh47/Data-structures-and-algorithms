# Problem 26 (Easy): https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}
        i = 0
        while(i < len(nums)):
            if(nums[i] not in freq):
                freq[nums[i]] = 1
                i += 1
            else:
                del nums[i]
        return i

if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().removeDuplicates(nums)) # 2
    print(nums) # [1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums)) # 5
    print(nums) # [0,1,2,3,4]
    nums = [1]
    print(Solution().removeDuplicates(nums)) # 1
    print(nums) # [1]
    nums = [1,2,4,5,6]
    print(Solution().removeDuplicates(nums)) # 5
    print(nums) # [1,2,4,5,6]
    nums = [1,1,1,1,1,1,1,1,1,1]
    print(Solution().removeDuplicates(nums)) # 1
    print(nums) # [1]
# Problem 80. Remove Duplicates from Sorted Array II (Medium): https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        freq = {}
        while (i < len(nums)):
            if(nums[i] not in freq):
                freq[nums[i]] = 1
                i += 1
            else:
                if(freq[nums[i]] > 1):
                    del nums[i]
                else:
                    freq[nums[i]] += 1
                    i += 1

        return i

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    print(Solution().removeDuplicates(nums)) # 5
    print(nums) # [1,1,2,2,3]
    nums = [0,0,1,1,1,1,2,3,3]
    print(Solution().removeDuplicates(nums)) # 7
    print(nums) # [0,0,1,1,2,3,3]
    nums = [1,1,1,1,1,1,1,1,1,1]
    print(Solution().removeDuplicates(nums)) # 2
    print(nums) # [1,1]
    nums = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
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

# hint: uses two pointers since the array is sorted
# no extra memory is used
class Solution2:
    def removeDuplicates(nums) -> int:
        start = 0   
        end = 0
        while (end < len(nums)):
            if(nums[end] == nums[start]):
                if(end - start < 2):
                    end += 1
                else:
                    del nums[end]
            else:
                start = end
        return len(nums)

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
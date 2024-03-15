# Problem 27 (Easy): https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        while(i < len(nums)):
            print(len(nums), i)
            if(nums[i] == val):
                del nums[i]
            else:
                i = i + 1
                count += 1
        return count

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    print(Solution().removeElement(nums, val)) # 2
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val)) # 5
    nums = [1]
    val = 1
    print(Solution().removeElement(nums, val)) # 0
    nums = [1,2,4,5,6]
    val = 3
    print(Solution().removeElement(nums, val)) # 5
# Problem 217: Contains Duplicate (Easy): https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        freq = {}
        containsDuplicate = False
        for i in range(len(nums)):
            num = nums[i]
            if(num not in freq):
                freq[num] = 1
            else:
                freq[num]+=1
                containsDuplicate = True
                break
        return containsDuplicate

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))
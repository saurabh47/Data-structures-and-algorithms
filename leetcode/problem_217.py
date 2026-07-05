# Problem 217: Contains Duplicate (Easy): https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums):
        freq = {}
        for number in nums:
            if(number in freq):
                return True
            else:
                freq[number] = 1
        return False

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if(num in s):
                return True   
            s.add(num)     
        return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))
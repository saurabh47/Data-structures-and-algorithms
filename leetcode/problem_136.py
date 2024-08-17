### Problem 136. Single Number (Easy)
### Tags: BitManipulation, HashTable

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
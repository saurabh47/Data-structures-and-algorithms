### Problem 260. Single Number III (Medium)
### Tags: array, bit manipulation

# Requires O(n) time complexity and O(n) space complexity
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        num1 = None
        num2 = None
        # 1 2 3 3
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        result = []
        for key, value in freq.items():
            if(value == 1):
                result.append(key)
        return result

# Optimized solution O(n) time complexity and O(1) space complexity

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        # [1, 2, 1, 3, 2, 5]    
        # XOR cancels out duplicates
        # and gives result of 3 ^ 5 = 6 (0110)
        # So we need to figure out 3, 5 from 6
        # bit `1` in 6 indicates one of the number (3, 5) has 1 in those places
        # 0011 and 0101
        # 00110
        # use diff bit to check which place has `1`
        # 00001, 00010, 000100
        diff_bit = 1
        while(not(xor & diff_bit)):
            diff_bit = diff_bit << 1
        # now we will iterate and divide the number in two groups
        # group a that has 1 in 10 ths place and group b that doesn't
        a = 0
        b = 0
        for num in nums:
            if(diff_bit & num):
                a = a ^ num
            else:
                b = b ^ num
        return [a, b]

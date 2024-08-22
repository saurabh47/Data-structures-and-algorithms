### Problem 476. Number Complement (Easy): https://leetcode.com/problems/number-complement/
### tags: bit manipulation, easy

# hint: mask to flip one digit at a time using XOR (^)
# << num to keep track of the number of bits to flip
class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        result = 0
        init = False
        while(num > 0):
            if(not init):
                result = num ^ mask
                init = True
            else:
                result = result ^ mask
            num >>= 1
            mask <<= 1
        return result
        # 0 0 0 0 0
        # 0 0 1 0 1
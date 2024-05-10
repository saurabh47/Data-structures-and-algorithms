# Problem 7: Reverse Integer (Easy): https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        isNegative = False
        if(x < 0):
            isNegative = True
        if(isNegative):
            x = x * -1
        while(x != 0 ):
            remainder = x % 10
            reverse = reverse * 10 + remainder 
            x = x // 10
        if(isNegative):
            reverse = reverse * -1
        if(reverse.bit_length() > 31):
            return 0
        return reverse

# Recursive solution
class Solution2:
    def reverse(self, x: int) -> int:
        result = self.reversed(abs(x), 0)
        print("result:", result)
        if(result.bit_length() > 31):
            return 0
        if(x < 0):
            result *= -1
        return result

    def reversed(self, x:int, result: int)->int:
        if(x < 1):
            return result
        result = (result * 10) + (x % 10)
        return self.reversed(x//10, result)

if __name__ == "__main__":
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
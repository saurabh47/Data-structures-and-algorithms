# Problem Statement: [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

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


if __name__ == "__main__":
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
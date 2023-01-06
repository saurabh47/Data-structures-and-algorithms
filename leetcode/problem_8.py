# Problem 8: String to Integer (atoi) (Medium): https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        isPositive = True
        result = 0
        s = s.strip()
        if(len(s) == 0 or not self.isNumber(s[0]) and not self.isOperator(s[0])):
            return 0
        for i in range(len(s)):
            letter = s[i]
            ascii = ord(letter)
            if(self.isOperator(letter) and len(s)-1 != i):
                if(letter == '-'):
                    isPositive = False
            elif(self.isNumber(letter)):
                result = result*10 + int(letter)
            else:
                break;
            if(len(s)-1 > i):
                if(self.isOperator(letter) and not self.isNumber(s[i+1])):
                    return 0
                elif(self.isNumber(letter) and self.isOperator(s[i+1])):
                    break
        if(not isPositive):
            result = result * -1
        if(result > (2**31) - 1):
           return 2**31 -1
        if(result < -(2**31)):
            return -(2**31)
        return result

    def isOperator(self, letter)->bool:
        return letter == '+' or letter == '-'

    def isNumber(self, letter)->bool:
        ascii = ord(letter)
        return ascii >= 48 and ascii <= 57

if __name__ == "__main__":
    print(Solution().myAtoi("42"))  # 42
    print(Solution().myAtoi("   -42")) # -42
    print(Solution().myAtoi("4193 with words")) # 4193
    print(Solution().myAtoi("words and 987")) # 0
    print(Solution().myAtoi("-91283472332")) # -2147483648
# Problem 9: Palindrome Number (Easy): https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        isNegative = x < 0
        if(isNegative):
            return False
        temp = abs(x)
        while(temp != 0):
            right = temp % 10
            result = result*10 + right
            temp = temp//10
        return result == x

if __name__ == "__main__":
    print(Solution().isPalindrome(121))  # True
    print(Solution().isPalindrome(-121)) # False
    print(Solution().isPalindrome(10)) # False
    print(Solution().isPalindrome(-101)) # False
    print(Solution().isPalindrome(0)) # True
    print(Solution().isPalindrome(11)) # True
    print(Solution().isPalindrome(1001)) # True
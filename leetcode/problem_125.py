# Problem 125: Valid Palindrome (Easy): https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        k = ""
        for i in range(len(s)):
            ascii = ord(s[i])
            if((ascii >= 97 and ascii <= 122) or (ascii >= 48 and ascii < 58)):
                k+=s[i]
        print(k)
        return k == k[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s)) # True


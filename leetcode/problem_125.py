# Problem 125: Valid Palindrome (Easy): https://leetcode.com/problems/valid-palindrome/

# Solution 1 using extra memory
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        k = ""
        for i in range(len(s)):
            ascii = ord(s[i])
            if((ascii >= 97 and ascii <= 122) or (ascii >= 48 and ascii < 58)):
                k+=s[i]
        return k == k[::-1]

#  Solution 2 using two pointers
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        if(len(s) == 0):
            return True
        start = 0
        end = len(s)-1
        while(end >= start):
            ascii_s = ord(s[start])
            ascii_e = ord(s[end])
            if(self.isAlphaNumeric(s[start])):
                if(self.isAlphaNumeric(s[end])):
                    if(s[start].lower() == s[end].lower()):
                        start += 1
                        end -= 1
                    else:
                        return False
                else:
                    end -=1
            else:
                start += 1
        return True

    def isAlphaNumeric(self, s:str)->bool:
        ascii_s = ord(s.lower())
        if((ascii_s >= 97 and ascii_s <= 122) or (ascii_s >= 48 and ascii_s < 58)):
             return True
        return False

# Time complexity: O(n)
# Space complexity: O(1)
class Solution3:
    def isPalindrome(self, s: str) -> bool:

        def isAlphaNumeric(letter: str):
            return (ord(letter) >= 97 and ord(letter) <= 122) or (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 48 and ord(letter) <= 57)

        start = 0
        end = len(s) - 1
        reverse = ''
        while(start < end):
            while(not isAlphaNumeric(s[start]) and start < len(s) - 1):
                start += 1
            while(not isAlphaNumeric(s[end]) and end > 0):
                end -= 1
            if(start >= end):
                return True
            if(s[start].lower() != s[end].lower()):
                return False
            start += 1
            end -= 1
        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s)) # True
    print(Solution2().isPalindrome(s)) # True




# Problem 5: Longest Palindromic Substring (Medium): https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        result =''
        if(len(s) < 2):
            return s
        for i in range(len(s)-1):
            maxPal1 = self.maxPalindromeLenAtIndex(i,i, s)
            maxPal2 = self.maxPalindromeLenAtIndex(i, i+1,s)
            maxPal = ''
            if(len(maxPal1) > len(maxPal2)):
                maxPal = maxPal1
            else:
                maxPal = maxPal2
            if(len(maxPal) > maxLen):
                maxLen = len(maxPal)
                result = maxPal
        return result

    def maxPalindromeLenAtIndex(self, b:int, e:int, s: str) -> str:
        maxLen = 0
        start = b
        end = e
        maxPal = ''
        while(start >= 0 and end < len(s) and s[start] == s[end]):
            strLen = end - start + 1
            subStr = s[start:end+1]
            if(strLen > maxLen):
                maxLen = strLen
                maxPal = subStr
            start -= 1
            end += 1
        return maxPal

# for each char in String expand outward
# same logic for even and odd string has to be repeated
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            start = i
            end = i
            while(start >= 0 and end < len(s) and s[start] == s[end]):
                if(len(result) < end - start + 1):
                    result = s[start : end+1]
                start -=1
                end += 1
            start = i
            end = i+1
            while(start >= 0 and end < len(s) and s[start] == s[end]):
                if(len(result) < end - start + 1):
                    result = s[start : end + 1]
                start -= 1
                end += 1
        return result


# Brute Force

class Solution3:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            return s == s[:: -1]
        if(len(s) < 2):
            return s
        max_len = 1
        result = s[0]
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if(j - i + 1 > max_len and isPalindrome(s[i:j+1])):
                    result = s[i:j+1]
                    max_len = j - i + 1
        return result


if __name__ == "__main__":
        s = Solution()
        print(s.longestPalindrome('ababcccbabb'))
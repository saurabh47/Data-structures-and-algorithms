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

if __name__ == "__main__":
        s = Solution()
        print(s.longestPalindrome('ababcccbabb'))
# Problem 3: Longest Substring Without Repeating Characters (Medium): https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        count = 0
        back = 0
        front = 0
        if(len(s)==0):
            return count
        while(front < len(s)):
            string = s[back:front]
            if(string.find(s[front]) == -1):
                front += 1
                count = max(count, len(string))
            else:
                back += 1
        return count+1

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s)) # 3
    
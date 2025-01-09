### Problem 1961. Check If String Is a Prefix of Array
### tags: array, two pointers, strings

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        count = 0
        index = -1
        con_s = ''
        for i in range(len(words)):
            count += len(words[i])
            con_s += words[i]
            if(count == len(s)):
                index = i
                break
        if(index == -1):
            return False
        return con_s == s

### Problem 2255. Count Prefixes of a Given String (Easy): https://leetcode.com/problems/count-number-of-words/

### tags: string, array
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        def is_prefix(word):
            i, j = 0, 0
            if(len(word) > len(s)):
                return False
            while(i < len(word) and j < len(s) and word[i] == s[j]):
                i += 1
                j += 1
            return i == len(word)

        count = 0
        for word in words:
            if(is_prefix(word)):
                count += 1
        return count
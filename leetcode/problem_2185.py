### Problem 2185. Counting Words With a Given Prefix (Easy): https://leetcode.com/problems/counting-words-with-a-given-prefix/

### tags: array, string, string matchings
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        wordCount = 0
        i = 0
        for word in words:
            if(len(word) < len(pref)):
                continue
            k = 0
            j = 0
            while(j < len(pref) and k < len(word) and word[k] == pref[j]):
                j += 1
                k += 1
            if(j == len(pref)):
                wordCount += 1
        return wordCount
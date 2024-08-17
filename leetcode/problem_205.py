### Problem 205. Isomorphic Strings (Easy): https://leetcode.com/problems/isomorphic-strings/
### Tags: String, Hash Table

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        lmap = {}
        mapped = {}
        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]
            if(letter_s in lmap):
                if(lmap[letter_s] != letter_t):
                    return False
            else:
                if(t[i] in mapped):
                    return False
                lmap[letter_s] = letter_t
                mapped[letter_t] = letter_s
        return True

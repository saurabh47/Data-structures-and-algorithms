### Problem 2486. Append Characters to String to Make Subsequence (Medium)
### Tags: String, Two Pointers, Greedy

# Hint: compare the characters of s and t, if they are equal, move both pointers, otherwise move only the pointer of s
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        count = 0
        while(i < len(s) and j < len(t)):
            if(s[i] == t[j]):
                i += 1
                j += 1
            else:
                i += 1
        if(i == len(s)):
            return len(t) - j
        else:
            return 0
### Problem 290. Word Pattern (Easy)
### Tags: Strings, Hash Table

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if(len(words) != len(pattern)):
            return False
        matches = {}
        rev_match = {}
        for index, word in enumerate(words):
            if((pattern[index] in matches) and matches[pattern[index]] != word):
                return False
            else:
                if((word in rev_match) and (rev_match[word] != pattern[index])):
                    return False 
                matches[pattern[index]] = word
                rev_match[word] = pattern[index]
        return True

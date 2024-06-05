### Problem 1002. Find Common Characters (Easy): https://leetcode.com/problems/find-common-characters/

### Tags: Array, Hash Table, String
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freqs = []
        for word in words:
            freq = {}
            for letter in word:
                if(letter not in freq):
                    freq[letter] = 1
                else:
                    freq[letter] += 1
            freqs.append(freq)
        result = []
        # check for any one freq
        for key, value in freqs[0].items():
            presentInAll = True
            minimum = value
            for i in range(1, len(freqs)):
                t = freqs[i]
                if(key not in t):
                    presentInAll = False
                    break
                else:
                    minimum = min(minimum, t[key])
            if(presentInAll):
                for i in range(minimum):
                    result.append(key)
        return result

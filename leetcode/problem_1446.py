### Problem 1446. Consecutive Characters (Easy): https://leetcode.com/problems/consecutive-characters/

### tags: String

class Solution:
    def maxPower(self, s: str) -> int:
        prev = s[0]
        count = 0
        result = 0
        for letter in s:
            if(letter == prev):
                count += 1
            else:
                count = 1
                prev = letter
            result = max(result, count)
        return result
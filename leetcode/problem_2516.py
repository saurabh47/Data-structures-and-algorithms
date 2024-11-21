### Problem 2516. Take K of Each Character From Left and Right Side (Medium): https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

### tags: hash table, sliding window, string

### hint: increase the window until we have k of each character, resulting string is outside of the window

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = Counter(s)
        if(not (freq['a'] >= k and freq['b'] >=k and freq['c'] >=k)):
            return -1

        start = 0
        result = float('inf')
        for end in range(len(s)):
            freq[s[end]] -=1
            while(freq['a'] < k or freq['b'] < k or freq['c'] < k):
                freq[s[start]] += 1
                start += 1
            
            result = min(result, len(s) - (end - start + 1))
        return result
            
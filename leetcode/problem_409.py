### Problem 409. Longest Palindrome (Easy)

### Tags: String, Hash Table, Greedy
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        freq = {}
        taken = {}
        for letter in s:
            if(letter not in freq):
                freq[letter] = 1
            else:
                freq[letter] += 1
        for key, value in freq.items():
            f = value // 2
            if(f > 0):
                taken[key] = f
                freq[key] -= f*2
            count += (f*2)
        for key, value in freq.items():
            if(value > 0 and key in taken):
                count += 1
                break
        if(count % 2 == 0 and count < len(s)):
            return count + 1
        return count
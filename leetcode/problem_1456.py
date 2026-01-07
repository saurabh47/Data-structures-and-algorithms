### Problem 1456.  Maximum Number of Vowels in a Substring of Given Length 
### tags: sliding window, two pointers
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        result = 0
        start = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # a b c i i i d e f
        for end in range(len(s)):
            if(s[end] in vowels):
                count += 1
            if(end - start + 1 > k):
                if(s[start] in vowels):
                    count -= 1
                start += 1
            if(end - start + 1 == k):
                result = max(count, result)
        return result
            
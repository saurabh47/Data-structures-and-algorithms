### Problem: Number of Substrings Containing All Three Characters (https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

### tags: string, sliding window

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        start = 0
        arr = [0, 0, 0]
        for end in range(len(s)):
            index = ord(s[end]) % 97
            arr[index] += 1
            while(arr[0] > 0 and arr[1] > 0 and arr[2] > 0):
                result += (len(s) - end)
                i = ord(s[start]) % 97
                arr[i] -= 1
                start += 1
        return result

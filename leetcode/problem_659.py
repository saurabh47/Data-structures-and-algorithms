### Problem 659. Encode and Decode Strings (Medium): https://leetcode.com/problems/encode-and-decode-strings/ (Premium)

### tags: string, encoding, decoding

class Solution:
    def encode(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""
        encoded = ""
        for s in strs:
            l = len(s)
            delimeter = '#'
            encoded += (str(l) + delimeter + s)
        return encoded

    def decode(self, s: str) -> List[str]:
        start = 0
        end = 0
        result = []
        while(end != len(s)):
            start = end
            while(s[end] != '#'):
                end += 1
            num = int(s[start:end])
            start = end + 1
            end += (num + 1)
            st = s[start: end]
            result.append(st)
        return result

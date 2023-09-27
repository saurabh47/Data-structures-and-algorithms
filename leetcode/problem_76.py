class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = len(t)-1;
        freq = self.countFreq(t)
        subStr = ''
        while(end != len(s)):
            subStr = s[start:end+1]
            if(self.containsSubstring(subStr,freq)):
                return subStr
            else:
                start += 1
                end += 1
        return subStr

    def countFreq(self, s):
        freq = {}
        for key in s:
            if(key not in freq):
                freq[key] = 1
            else:
                freq[key] = freq[key]+1
        return freq

    def containsSubstring(self, s, t):
        for key, value in t.items():
            if(s.count(key) != t[key]):
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC")) # BANC



# Problem 424: Longest Repeating Character Replacement (Medium): https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        result =''
        skip = k
        freq = {}
        while(end != len(s)):
            if(len(s[start:len(s)]) < len(result)):
                break
            if(s[end] not in freq):
                freq[s[end]] = 1
            currentStr = s[start:end+1]
            length = end - start + 1
            maxfreq = self.maxFreq(freq)
            if(length - maxfreq <= k):
                end+=1
                if(end < len(s)): 
                    if s[end] not in freq:
                        freq[s[end]] = 1
                    else:
                        freq[s[end]] += 1
                if(len(currentStr) > len(result)):
                    result = currentStr
            else:
                freq[s[start]] -= 1
                start+=1
        return len(result)

    def maxFreq(self, freq):
        m = 0
        for i, (key, value) in enumerate(freq.items()):
            if(value > m):
                m = value
        return m

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    print(Solution().characterReplacement(s,k)) # 4
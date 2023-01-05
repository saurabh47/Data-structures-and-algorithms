# Problem 242: Valid Anagram (Easy): https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        freq_s = {} 
        freq_k = {}
        for i in range(len(s)):
            letter_i = s[i]
            letter_k = t[i]
            if(letter_i in freq_s):
                freq_s[letter_i] +=1
            else:
                freq_s[letter_i] = 1
            if(letter_k in freq_k):
                freq_k[letter_k] +=1
            else:
                freq_k[letter_k] = 1
        result = True
        for key,value in freq_s.items():
            if(key not in freq_k or freq_s[key]!=freq_k[key]):
                result = False
                break;
        return result

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s,t)) # True

# Problem 383. Ransom Note (https://leetcode.com/problems/ransom-note/)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = {}
        freq2 = {}
        for letter in ransomNote:
            if letter not in freq1:
                freq1[letter] = 1
            else:
                freq1[letter] += 1

        for letter in magazine:
            if letter not in freq2:
                freq2[letter] = 1
            else:
                freq2[letter] += 1
        for key, value in freq1.items():
            if((key not in freq2) or ((key in freq2) and freq2[key] < value)):
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct("a", "b")) # False
    print(s.canConstruct("aa", "ab")) # False
    print(s.canConstruct("aa", "aab")) # True
                         
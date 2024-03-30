# Problem 451. Sort Characters By Frequency (Medium): https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in range(len(s)):
            char = s[i]
            if(char not in freq):
                freq[char] = 1
            else:
                freq[char] += 1
        result = sorted([(v, k) for k, v in freq.items()], reverse=True)
        temp = ''
        for i in range(len(result)):
            tup = result[i]
            temp += (tup[1]*tup[0])
        return temp
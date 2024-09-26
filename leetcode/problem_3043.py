### Problem 3043. Longest Common Prefix (Medium): https://leetcode.com/problems/longest-common-prefix/

### tags: array, hashtable, string, trie
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for num in arr2:
            while(num != 0):
                prefixes.add(num)
                num //= 10

        max_len = 0
        for num in arr1:
            if(num in prefixes):
                max_len = max(max_len, len(str(num)))
            else:
                while(num != 0):
                    if(num in prefixes):
                        max_len = max(max_len, len(str(num)))
                        break
                    num //= 10
        return max_len



# Problem 392: Is Subsequence (https://leetcode.com/problems/is-subsequence/)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0, 0
        if(len(s) == len(t)):
            return s == t
        while(i < len(s) and j < len(t)):
            if(s[i] == t[j]):
                i += 1
                j += 1
            else:
                j += 1
        return len(s) == i

if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence("abc","ahbgdc")) # True
    print(s.isSubsequence("axc","ahbgdc")) # False
    print(s.isSubsequence("abc","abc")) # True
    print(s.isSubsequence("abc","ahbgdc")) # True
    print(s.isSubsequence("","ahbgdc")) # True
    print(s.isSubsequence("","")) # True
    print(s.isSubsequence("a","")) # False
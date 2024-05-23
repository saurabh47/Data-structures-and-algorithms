### Problem 344. Reverse String (Easy): https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.reversed(0, len(s)-1, s)
    
    def reversed(self, start:int, end:int, s: List[str])-> List[str]:
        if(start >= end):
            return s
        else:
            temp = s[end]
            s[end] = s[start]
            s[start] = temp
            return self.reversed(start + 1, end - 1, s)
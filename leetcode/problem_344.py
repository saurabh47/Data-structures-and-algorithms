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

### Iterative
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while(start < end):
            temp = s[end]
            s[end] = s[start]
            s[start] = temp
            start += 1
            end -= 1
        return s

class Solution3:
    def reverseString(self, s: List[str]) -> None:
        # 
        # INPUT = ["h","e","l","l","o"]
        # OUTPUT = ["o","l","l","e","h"]
        # ["h","e","l","l","o"]
        # ["o","e","l","l","h"]
        # ["o","l","l","e","h"]

        start = 0 
        end = len(s) - 1
        while(start < end):
            if(s[start] != s[end]):
                self.swap(s, start, end)
            start += 1
            end -= 1 
    
    def swap(self, s: List[str], start, end):
        temp = s[start]
        s[start] = s[end]
        s[end] = temp



        
### Problem 2696:Minimum String Length After Removing Substrings (Easy): https://leetcode.com/problems/minimum-string-length-after-removing-substrings

### tags: stack
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        end = 0
        while(end != len(s)):
            if(not stack):
                stack.append(s[end])
            else:
                stack.append(s[end])
                top = "".join(stack[-2:])
                if(top == 'AB' or top == "CD"):
                    stack.pop()
                    stack.pop()
            end += 1
        return len(stack)
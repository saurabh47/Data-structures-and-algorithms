# Problem 20: Valid Parentheses (Easy): https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if(s[i] == '{' or s[i] == '(' or s[i] == '['):
                stack.append(s[i])
            elif(s[i]==')' or s[i]=='}' or s[i]==']'):
                 if(len(stack) == 0):
                     return False
                 else:
                     if((s[i]==')' and stack[-1] == '(') or (s[i]=='}' and stack[-1] == '{') or (s[i]==']' and stack[-1] == '[')):
                         stack.pop()
                     else:
                         return False
        return len(stack) == 0
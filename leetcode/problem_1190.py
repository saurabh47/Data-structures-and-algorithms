### Problem 1190. Reverse Substrings Between Each Pair of Parentheses (Medium): https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
### Tags: Stack
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if(c != ')'):
                stack.append(c)
            else:
                result = ''
                while(stack[-1] != '('):
                    result += stack.pop()
                stack.pop()
                for k in result:
                    stack.append(k)
        return ''.join(stack)
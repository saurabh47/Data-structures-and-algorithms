# Problem 13. Roman to Integer (Easy): https://leetcode.com/problems/roman-to-integer/
# hint: The key intuition lies in the fact that in Roman numerals, when a smaller value appears /
# before a larger value, it represents subtraction e.g IV = > V - I, while when a smaller value appears after or equal to a larger value, it represents addition VI = V + I .
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M': 1000,
        }
        number = 0
        i = 0
        while(i < len(s)):
            if(i == len(s) - 1):
                number += symbols[s[i]]
            elif(symbols[s[i]] < symbols[s[i+1]]):
                number += symbols[s[i+1]] - symbols[s[i]]
                i += 1
            else:
                number += symbols[s[i]]
            i += 1
        return number

class Solution2:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M': 1000,
        }
        number = 0
        i = 0
        while(i < len(s)):
            if(i == len(s) - 1):
                number += symbols[s[i]]
            elif(s[i] == 'I' and s[i+1] =='V'):
                number += 4
                i += 1
            elif(s[i] == 'I' and s[i+1] =='X'):
                number += 9
                i += 1
            elif( s[i] == 'X' and s[i+1] =='L'):
                number += 40
                i += 1
            elif(s[i] == 'X' and s[i+1] =='C'):
                number += 90
                i += 1
            elif(s[i] == 'C' and s[i+1] =='M'):
                number += 900
                i += 1
            elif(s[i] == 'C' and s[i+1] =='D'):
                number += 400
                i += 1
            else:
                number += symbols[s[i]]
            i += 1
            print(number, i)
        return number
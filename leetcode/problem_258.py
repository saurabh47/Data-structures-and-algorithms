### Problem 258. Add Digits (Easy): https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        while(num > 9):
            sum = 0
            while(num != 0):
                sum += num % 10
                num = num // 10
            num = sum
        return num
### Problem 1963. Minimum Number of Swaps to Make the String Balanced (Medium): https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced

class Solution:
    def minSwaps(self, s: str) -> int:
        result = 0
        maxClose = 0
        for bracket in s:
            if(bracket == '['):
                result -= 1
            else:
                result += 1
            maxClose = max(result, maxClose)
        return (maxClose + 1) // 2
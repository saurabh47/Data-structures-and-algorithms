### problem 1869. Longer Contiguous Segments of Ones than Zeros (Easy): https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
### tags : String
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count_one = 0
        count_zero = 0
        result_one = 0
        result_zero = 0
        for letter in s:
            if(letter == '1'):
                count_one += 1
                count_zero = 0
            else:
                count_one = 0
                count_zero += 1
            result_one = max(result_one, count_one)
            result_zero = max(result_zero, count_zero)
        return result_one > result_zero
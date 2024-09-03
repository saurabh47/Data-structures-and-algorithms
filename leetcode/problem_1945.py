### Problem 1945. Sum of Digits of String After Convert (Easy): https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

### tags: string, simulation
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def str_sum(sno):
            sum_n=0
            for n in sno:
                sum_n += int(n)
            return sum_n
        numbers = ''
        for ch in s:
            numbers += str((ord(ch) % 97) + 1)

        result = 0
        while(k > 0):
            result = str_sum(numbers)
            numbers = str(result)
            k -= 1
        return result
### Problem 2582. Pass the Pillow (Easy): https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if(time < n):
            return time + 1
        elif(time == n):
            return n - 1
        else:
            pos = 1
            inc = 1
            for i in range(time):
                if(pos == n and inc == 1):
                    inc *= -1
                if(pos == 1 and inc == -1):
                    inc *= -1
                pos += inc
            return pos
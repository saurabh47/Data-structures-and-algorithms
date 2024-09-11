### Problem 1318. Minimum Flips to Make a OR b Equal to c
### tags: bit manipulation

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # a =    0010
        # b =    0110
        # a | b= 0110
        # 0101
        count = 0
        while(c > 0 or a > 0 or b > 0):
            if(c & 1 == 0):
                if(a & 1 and b & 1):
                    count += 2
                elif(a & 1 or b & 1):
                    count += 1
            else:
                if((a & 1 == 0) and (b & 1 == 0)):
                    count += 1
            c >>= 1
            a >>= 1
            b >>= 1 
        return count
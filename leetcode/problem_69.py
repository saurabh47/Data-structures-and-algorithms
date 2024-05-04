### Problem 69. Sqrt(x) (https://leetcode.com/problems/sqrtx/)

class Solution:
    def mySqrt(self, x: int) -> int:
        if( x == 0 or x == 1):
            return x
        start = 1
        end = x
        while(start <= end):
            mid = start + ((end - start) // 2)
            square = mid * mid
            if(square == x):
                return mid
            elif(square > x):
                end = mid - 1
            else:
                start = mid+1
        return round(end)
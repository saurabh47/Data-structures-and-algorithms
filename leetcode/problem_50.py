class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n == 0):
            return 1
        if(n < 0):
            return 1 / (x * self.myPow(x, -n - 1))
        if( n % 2 == 0):
            ans = self.myPow(x, n // 2)
            return ans * ans
        return x * self.myPow(x, n-1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        k = n
        if( n == 0):
            return result
        if( x == 0):
            return 0
        if(n < 0):
            k = abs(n)
            x = 1 / x
        while(k > 0):
            if(k % 2 == 0):
                k = k // 2
                x = x * x
            else:
                result *= x
                k -= 1
        return result
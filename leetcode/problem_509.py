### Problem 509. Fibonacci Number (Easy)
### Tags: Dynamic Programming

class Solution:
    def fib(self, n: int) -> int:
        # 0 1 1 2 3 5
        x, y = 0, 1
        z = 0
        if(n == 0):
            return n
        if(n < 3):
            return 1
        for i in range(2,n+1):
            z = x + y
            x = y
            y = z
        return z
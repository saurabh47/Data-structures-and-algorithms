### Problem 263. Ugly Number

### Tags: Math, Recursion

class Solution:
    def isUgly(self, n: int) -> bool:
        if(n == 1):
            return True
        if(n < 1):
            return False
        if(n % 2 == 0):
            return self.isUgly(n//2)
        elif(n % 3 == 0):
            return self.isUgly(n//3)
        elif(n % 5 == 0):
            return self.isUgly(n//5)
        else:
            return False
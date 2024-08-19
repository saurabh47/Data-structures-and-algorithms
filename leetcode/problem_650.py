### Problem 650. 2 Keys Keyboard (Medium)
### tags: Dynamic Programming

class Solution:
    def minSteps(self, n: int) -> int:
        # Function f(n) `n` denotes number of inputs and
        # f(n) outputs the number of operations to get n `A`s
        # f(1) = 0
        # f(2) = c1 + p1 = 2, AA
        # f(3) = f(2) + p1 = 3 AAA
        # f(4) = f(3) + p1 = 4, AAAA 
        # f(5) = f(4) + p1 = 5,  AAAAA
        # f(6) = f(3) + c1 + p1 = 5
        # f(7) = f(5) + p2 = 7
        # f(8) = f(4) + c1 + p1 = 6
        # f(9) = f(7) + p2 = 9
        # f(10) = f(5) + c1 + p1 = 7
        # f(25) = f(5) + c1 + p4 = 10
        # f(125) = f(25) + c1 + p4 = 15
        # 12
        chars = 1
        copy = 0
        operations = 0
        while(chars != n):
            if(n % chars == 0):
                copy = chars
                operations += 1
            chars += copy
            operations += 1
            print("operation:", operations, "chars:", chars, "copy:",copy)
        return operations
        
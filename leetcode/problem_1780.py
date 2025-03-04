#### Problem 1780. Check if Number is a Sum of Powers of Three
### tags: [backtracking]

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(x, s):
            if(s == n):
                return True
            if(s > n or 3**x > n):
                return False
            else:
                if(backtrack(x+1, s + 3**x)):
                    return True
                return backtrack(x+1, s)

        return backtrack(0, 0)    

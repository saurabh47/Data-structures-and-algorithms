# Problem 202. Happy Number (Easy): https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        result = 0
        count = 0
        visited = {}
        while(n != 1):
            while(n != 0):
                rem = n%10
                n = n//10
                result += pow(rem, 2)
            count +=1
            n = result
            result = 0
            # If we encounter the same number again, then it will go into an infinite loop
            if(n in visited):
                return False
            else:
                visited[n] = True
        return True
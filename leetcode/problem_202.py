# Problem 202. Happy Number (Easy): https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        result = 0
        count = 0
        while(n != 1):
            while(n != 0):
                rem = n%10
                n = n//10
                result += pow(rem, 2)
            count +=1
            n = result
            result = 0
            # If it is in endless loop for more than 10 times, then it is not a happy number
            if(count > 10):
                return False
        return True
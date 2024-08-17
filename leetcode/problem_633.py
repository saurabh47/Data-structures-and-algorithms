### Problem. 633 Sum of Square Numbers (Easy): https://leetcode.com/problems/sum-of-square-numbers/

### Tags: Math, Two Pointers
### Similar to Problem 167. Two Sum II - Input array is sorted (Easy): https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        hs = {}
        for i in range(int(sqrt(c))+1):
            hs[i*i] = i
            target = c - i*i
            if(target in hs):
                return True
        return False
    
### Two pointer approach

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        while(a <= b):
            if(a*a + b*b < c):
                a+=1
            elif(a*a + b*b > c):
                b-=1
            else:
                return True
        return False
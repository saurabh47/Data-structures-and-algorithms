### Problem 70. Climbing Stairs (Easy)
### Tags: Dynamic Programming

class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 1, 2]
        if(n < 2):
            return 1
        elif(n == 2):
            return 2
        else:
            for i in range(3, n+1):
                arr.append(arr[i-1] + arr[i-2])
        return arr[n-1] + arr[n-2]



### Approach:
# Find the base cases
# f(0) = 1
# f(1) = 1
# f(2) = 2
# f(3) = f(1) + f(2)
# This approach is called bottom-up approach
# We can get to 3rd step from either
# 1st step + 2 steps
# 2nd step + 1 step
# Since we can only take 1 or 2 steps at a time
# Hence f(3) = f(1) + f(2)
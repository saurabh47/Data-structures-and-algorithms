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


### Optimized on Memory
# Uses only use two variables instead of allocating an array
# since we only need the last two values to calculate the next value
class Solution2:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 2
        if(n < 2):
            return 1
        elif(n == 2):
            return 2
        else:
            for i in range(3, n):
                # arr.append(arr[i-1] + arr[i-2])
                z = x + y
                x = y
                y = z
        return x + y

    def climb3Stairs(n):
        x = 1
        y = 2
        z = 4
        if(n < 2):
            return 1
        elif(n == 2):
            return 2
        elif(n == 3):
            return 4
        else:
            for i in range(4, n):
                k = x + y + z
                x = y
                y = z
                z = k
        return x + y + z

print(climb3Stairs(5))

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
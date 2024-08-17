# Given n as input find the sum of all numbers from 1 to n

### Topic: Dynamic Programming
# f(1) => 1
# f(2) => 1 + 2 = 3 = f(1) + 2
# f(3) => 1 + 2 + 3 = 6 = f(2) + 3
# f(4) => 1 + 2 + 3 + 4 = 10 = f(3) + 4
def sum_n(n):
    if(n == 1):
        return 1
    return sum_n(n-1) + n

# The Issue with above approach is we are recalculating the sum of all numbers from 1 to n-1 multiple times. So we can use memoization to store the result of sum of all numbers from 1 to n-1 and use it to calculate sum of all numbers from 1 to n in O(n) time complexity.
def sum_n(n):
    if(n == 1):
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + i
    return dp[n]


print(sum_n(4)) # 10


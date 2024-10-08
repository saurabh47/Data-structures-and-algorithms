# fibonacci Series
# 0 1
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0) = 1
# f(3) = f(2) + f(1) = 2
# f(n) = f(n-1) + f(n-2)
# n is the nth number in the fibonacci series

def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memoization(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# further optimization can be done by using two variables instead of an array
def fib(n):
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

if __name__ =='__main__':
    print(fibonacci(5)) # 5
    print(fibonacci(10)) # 55
    print(fibonacci_memoization(10)) # 55
    print(fib(10)) # 55


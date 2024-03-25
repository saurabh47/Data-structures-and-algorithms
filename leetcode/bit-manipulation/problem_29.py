# Problem 29. Divide Two Integers (Medium)

# explanation: division is basically subtraction quotient times
# but doing so will take O(n) time where n is the quotient
# But when the number is large, it will take long time subtracting the divisor from dividend
# imagine 1M/1, it will take 1M iterations to get the quotient
# so we can use bit manipulation to reduce the time complexity
# we can subtract the divisor from dividend in multiple of 2
# so that we can reduce the time complexity to O(log(n))
# e.g 1M/1 we can subtract 512K, 256K, 128K, 64K, 32K, 16K, 8K, 4K, 2K, 1K, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1 from dividend and simultaneously add 512K, 256K, 128K, 64K, 32K, 16K, 8K, 4K, 2K, 1K, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1 to quotient

# handrun
# 58/4 = 14
# quotient = 0
# dividend = 58
# 4 * 2^0 = 4 < 58
# 4 * 2^1 = 8 < 58
# 4 * 2^2 = 16 < 58
# 4 * 2^3 = 32 < 58 (add 1 << 3 to quotient)
# 4 * 2^4 = 64 < 58 (False)

# quotient = 8 # 8
# dividend = 58 - 32 = 26

# 4 * 2^0 = 4 < 26
# 4 * 2^1 = 8 < 26
# 4 * 2^2 = 16 < 26 (add 1 << 2 to quotient)
# 4 * 2^3 = 32 < 26 (False)

# quotient = 12  # 8 + 4
# dividend = 26 - 16 = 10

# 4 * 2^0 = 4 < 10
# 4 * 2^1 = 8 < 10 (add 1 << 1 to quotient)
# 4 * 2^2 = 16 < 10 (False)

# quotient = 14 # 8 + 4 + 2
# dividend = 10 - 8 = 2

# 4 * 2^0 = 4 < 2 (False) 

# quotient = 14 # 8 + 4 + 2
# dividend = 2 - 2 = 0

# return 14




class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        quotient = 0
        if(dividend == divisor):
            return 1
        if(xor(dividend < 0, divisor < 0)):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while(dividend >= divisor):
            i = 0
            while((divisor << (i+1)) < dividend):
                i+=1
            quotient += 1<<i
            dividend -= divisor << i
        if(sign == -1):
            quotient *= -1
        if(quotient > ((1 << 31) - 1)):
            quotient = (1 << 31) - 1
        if(quotient < -((1 << 31) - 1)):
            quotient = -(1 << 31)
        return quotient

    def xor(self, a , b):
        return (a and not b) or (not a and b)

if __name__ == "__main__":
    obj = Solution()
    print(obj.divide(10, 3)) # 3
    print(obj.divide(7, -3)) # -2
    print(obj.divide(0, 1)) # 0
    print(obj.divide(1, 1)) # 1
    print(obj.divide(1, 2)) # 0
    print(obj.divide(-1, 1)) # -1
    print(obj.divide(-1, -1)) # 1
    print(obj.divide(-1, -2)) # 0
    print(obj.divide(-1, 2)) # 0
    print(obj.divide(1, -2)) # 0


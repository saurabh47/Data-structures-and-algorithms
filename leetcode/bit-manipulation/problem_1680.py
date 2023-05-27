# Problem Title: Concatenation of Consecutive Binary Numbers
# Link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
# Approach: Shift result by length of binary i, Add i to result
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        for i in range(1,n+1):
            length = 0
            target = i
            while(target):
                target = target >> 1
                length+=1
            result <<= length
            result = (result | i) % (10**9 + 7)
        return result


# Optimized to not calculate length of binary i with a while loop
class Solution2:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        for i in range(1,n+1):
            # find length of binary i
            length = len(bin(i)) - 2
            result <<= length
            result = (result | i) % (10**9 + 7)
        return result




if __name__ == '__main__':
    solution = Solution()
    print(solution.concatenatedBinary(1)) # 1
    print(solution.concatenatedBinary(3)) # 27
    print(solution.concatenatedBinary(12)) # 505379714

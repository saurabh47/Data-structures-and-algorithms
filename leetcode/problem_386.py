### Problem 386. Lexicographical Numbers (Medium): https://leetcode.com/problems/lexicographical-numbers/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = []
        def dfs(x):
            if(x > n):
                return
            nums.append(x)
            x *= 10
            for i in range(10):
                dfs(x+i)

        for i in range(1,10):
            dfs(i)
        return nums

# Optimized
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = []
        stack = []
        x = 1
        seen = {}
        while len(nums) < n:
            nums.append(x)
            if(x * 10 <= n):
                x *= 10
            else:
                while(x == n or x % 10 == 9):
                    x = x // 10
                x += 1
        return nums
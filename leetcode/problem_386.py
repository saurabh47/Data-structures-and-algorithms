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
### Problem 1894. Find the Amount of Chalk Used (Medium): https://leetcode.com/problems/find-the-amount-of-chalk-used/

### tags: array, binary search, prefix sum
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if(len(chalk) == 1):
            return 0
        total = sum(chalk)
        while(k > total):
            k -= total
        if(k == total):
            return 0
        
        for i in range(len(chalk)):
            c  = chalk[i]
            if(c > k):
                return i
            k -= c
        return len(chalk) - 1

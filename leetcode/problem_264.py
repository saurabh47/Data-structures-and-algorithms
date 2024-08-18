### Problem 264. Ugly Number II (Medium): https://leetcode.com/problems/ugly-number-ii/
### tags: heap, dynamic programming
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set()
        heap = [1]
        i = 1
        factors = [2, 3, 5]
        for i in range(n):
            num  = heapq.heappop(heap)
            if(i == n - 1):
                return num
            for f in factors:
                if(f * num not in seen):
                    seen.add(num * f)
                    heapq.heappush(heap, num * f)
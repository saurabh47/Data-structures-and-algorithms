### Problem 2558. Pick Gifts (Medium)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        result = 0
        max_h = []
        for i in range(len(gifts)):
            result += gifts[i]
            heapq.heappush(max_h, gifts[i]*-1)
        for i in range(k):
            max_g = -1 * heapq.heappop(max_h)
            g = math.floor(math.sqrt(max_g))
            heapq.heappush(max_h, -1 * g)
            result = result - max_g + g
        return result
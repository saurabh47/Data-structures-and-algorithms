#### Problem 3264. Final Array State After K Multiplication Operations I
### tags: heap, array
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_h = []
        for i in range(len(nums)):
            heapq.heappush(min_h, (nums[i], i))
        
        for i in range(k):
            min_val, index = heapq.heappop(min_h)
            heapq.heappush(min_h,(min_val * multiplier, index))
            nums[index] = min_val * multiplier
        return nums
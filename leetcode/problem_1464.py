

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        return (nums[0] - 1) * (nums[1] - 1)

class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        max_heap = []
        for element in nums:
            heapq.heappush(max_heap, -element)
        n1 = (heapq.heappop(max_heap) * -1) - 1 
        n2 = (heapq.heappop(max_heap) * -1) - 1 
        return n1 * n2
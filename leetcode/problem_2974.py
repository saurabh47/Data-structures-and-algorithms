### Problem 2974. Minimum Number Game (Easy)

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []
        while(len(nums) > 0):
            sm_alice = heapq.heappop(nums)
            sm_bob = heapq.heappop(nums)
            result.append(sm_bob)
            result.append(sm_alice)
        return result
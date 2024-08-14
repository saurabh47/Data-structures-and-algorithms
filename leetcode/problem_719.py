### Problem 719. Find K-th Smallest Pair Distance
### tags: Two pointers, Binary Search, Array

### Brute force (Time limit exceeded 17/19)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        diff_heap = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff  = abs(nums[i]-nums[j])
                heapq.heappush(diff_heap, diff)
        while(k != 1):
            heapq.heappop(diff_heap)
            k-=1 
        return heapq.heappop(diff_heap)
    

class Solution2:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = max(nums)
        while(left < right):
            mid = left + ((right- left) // 2)
            l = 0
            count = 0
            for r in range(len(nums)):
                while(nums[r] - nums[l] > mid):
                    l += 1
                count += (r - l)

            if(count >= k):
                right = mid
            else:
                left = mid + 1
        return right


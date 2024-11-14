### Problem 875. Koko Eating Bananas (Medium): https://leetcode.com/problems/koko-eating-bananas/
### tags: binary search, math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eating_time(speed):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/speed)
            return hrs
            
        start = 1
        end = max(piles)
        speed = end
        while(start <= end):
            mid = start + (end - start) // 2
            time = eating_time(mid)
            if(time <= h):
                speed = min(speed, mid)
                end = mid - 1
            else:
                start = mid + 1 
        return speed
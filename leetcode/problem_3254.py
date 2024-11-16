### Problem 3254. Find the Power of K-Size Subarrays I
### tags: array, sliding window
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
    
        def isConsecutive(start, end):
            while(start <= end):
                if(start < end and (nums[start + 1] - nums[start]) != 1):
                    return False
                start += 1
            return True

        start = 0
        end = k - 1
        maximum = nums[end]
        result = []
        while(end != len(nums)):
            maximum = nums[end]
            if(isConsecutive(start, end)):
                result.append(maximum)
            else:
                result.append(-1)
            start += 1 
            end += 1
        return result

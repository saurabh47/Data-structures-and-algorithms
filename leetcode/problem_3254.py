### Problem 3254. Find the Power of K-Size Subarrays I
### tags: array, sliding window

# hint1: maximum will be last element in the current window
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

# Optimized
class Solution2:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        start = 0
        end = 0
        result = []
        cons_window_len = 1
        while(end != len(nums)):
            if(end > 0 and nums[end] - nums[end - 1] == 1):
                cons_window_len += 1
            
            if(end - start + 1 > k):
                if(nums[start + 1] - nums[start] == 1):
                    cons_window_len -= 1
                start += 1

            if(end - start + 1 == k):
                if(cons_window_len == k):
                    result.append(nums[end])
                else:
                    result.append(-1)
            end += 1
        return result


### Problem 2529.  Maximum Count of Positive Integer and Negative Integer (easy)
### tags: array, binary search

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # find index of first positive number or -1
        # pos = min(len(nums), index)
        # neg = max(0,index - 1)
        def findSmallestPositiveIndex(start, end):
            mid = start + (end - start) // 2 
            if(start == end):
                if(nums[start] < 1):
                    return -1
                else:
                    return start
            if(nums[mid] > 0):
                if(mid == start or nums[mid - 1] <= 0):
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1
            return findSmallestPositiveIndex(start, end)
        
        def findLargestNegativeIndex(start, end):
            if(start > end):
                return -1
            mid = start + (end - start) // 2 
            if(nums[mid] < 0):
                if mid == end or nums[mid + 1] >= 0:
                    return mid
                else:
                    start = mid + 1
            else:
                end = mid - 1
            return findLargestNegativeIndex(start, end)

        # main
        pos, neg = 0, 0
        index = findSmallestPositiveIndex(0, len(nums) - 1)
        neg_index = findLargestNegativeIndex(0, len(nums) - 1)
        
        if(index >= 0):
            pos = (len(nums) - index)
    
        if(neg_index >= 0):
            neg = neg_index + 1
            
        return max(pos, neg)


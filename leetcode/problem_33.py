# Problem 33. Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)-1;
        pivot = self.pivot(start, end, nums);
        print("start={}, end= {},pivot={}".format(start, end, pivot))
        array1 = nums[:pivot+1]
        array2 = nums[pivot+1:]
        print("array1={} array2={}".format(array1,array2))
        if(len(array1) > 0 and array1[0] <= target):
            # search left half
            return self.binarySearch(start, pivot, nums, target)
        else:
            # search right half
            return self.binarySearch(pivot+1, end, nums, target)

    def binarySearch(self, start, end, nums, target):
        if(end < start):
            return -1
        mid = (end + start)//2
        if(nums[mid] == target):
            return mid;
        elif(nums[mid] > target):
            return self.binarySearch(start, mid-1, nums, target)
        else:
            return self.binarySearch(mid+1, end, nums, target)

    def pivot(self, start, end, nums):
        if(start == end):
            return start
        mid = (end + start)// 2 #floor division
        # if array is sorted (no rotation)
        if(nums[mid] > nums[start] and nums[end] > nums[mid]):
            return end;
        if(nums[mid] > nums[mid+1]):
            return mid
        elif(nums[mid] < nums[mid-1] ):
            return mid - 1
        else:
            # mid < mid + 1
            # mid > mid -1
            if(nums[start] > nums[mid]):
                end = mid-1
            else:
                start = mid+1
            return self.pivot(start,end,nums)

if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4,5,6,7,0,1,2], 0)) # 4
    print(solution.search([4,5,6,7,0,1,2], 3)) # -1
    print(solution.search([1], 0)) # -1
    print(solution.search([1,3], 3)) # 1
    print(solution.search([3,1], 1)) # 1
    print(solution.search([5,1,3], 5)) # 0
    print(solution.search([5,1,3], 1)) # 1

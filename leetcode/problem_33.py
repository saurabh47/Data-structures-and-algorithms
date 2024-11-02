# Problem 33. Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# The Ideas is to apply binary search on a partial array
# We do this by finding the pivot point which basically divides the array into two
# subarray so as to be able to apply a binary search on either side of the array
# depending on where the target value lies.
# E.g [4,5,6,7,0,1,2] pivot = 4
# array1 = [4,5,6,7] array2 = [0,1,2]
# if target between start and pivot, we apply binary search on left half else right half

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def partition(start, end):
            while(start <= end):
                mid = start + (end - start) // 2
                if(start == end):
                    return start
                if(mid >= 0 and nums[mid] > nums[end]):
                    start = mid + 1
                if(nums[mid] <= nums[end]):
                    end = mid
            return start

        def bSearch(start, end):
            while(start <= end):
                mid = start + (end - start) // 2
                if(nums[mid] == target):
                    return mid
                if(target < nums[mid]):
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        start = 0
        end = len(nums) - 1
        index = partition(0, len(nums) - 1)
        if(nums[index] == target):
            return index
        if(nums[index]<= target and target <= nums[end]):
            return bSearch(index, end)
        else:
            return bSearch(start, index - 1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4,5,6,7,0,1,2], 0)) # 4
    print(solution.search([4,5,6,7,0,1,2], 3)) # -1
    print(solution.search([1], 0)) # -1
    print(solution.search([1,3], 3)) # 1
    print(solution.search([3,1], 1)) # 1
    print(solution.search([5,1,3], 5)) # 0
    print(solution.search([5,1,3], 1)) # 1

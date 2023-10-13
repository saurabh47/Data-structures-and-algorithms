# Problem 154 - Find Minimum in Rotated Sorted Array II
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        if(start == end):
            return nums[start]
        pivot = self.findPivot(start, end, nums)
        if(pivot == end):
            return nums[start]
        else:
            return nums[pivot+1]

    def findPivot(self, start, end, nums):
        mid = (start + end) // 2
        if(nums[mid] > nums[start] and nums[end] > nums[mid]):
            return end;
        if(nums[mid] < nums[mid-1]):
            return mid -1
        elif(nums[mid+1] < nums[mid]):
            return mid
        else:
            if(nums[mid] > nums[start]):
                return self.findPivot(mid+1, end, nums)
            else:
                return self.findPivot(start, mid, nums)

# Time Complexity: O(log n)

if __name__ == '__main__':
    solution = Solution()
    solution.findMin([3,4,5,1,2]) # 1
    solution.findMin([4,5,6,7,0,1,2]) # 0
    solution.findMin([2,2,2,0,1]) # 0
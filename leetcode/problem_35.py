# Problem 35: Search Insert Position (Easy): https://leetcode.com/problems/search-insert-position/

def searchInsert(self, nums, target: int) -> int:
    if(target not in nums):
        nums.append(target)
        nums = sorted(nums)
    start = 0
    end = len(nums) - 1
    mid = (end + start) //2
    print("nums=", nums, "target=", target, "mid = ", mid)
    while(nums[mid] != target):
        print("start=", start, "end = ",end, "mid = ", mid)
        # if(end-start==1 and target > nums[start] and target < nums[end]):
        #     return start+1
        if(nums[mid] > target):
            end = mid-1
        else:
            start = mid+1
        mid = (end + start) //2
    return mid

# Binary Search Solution (O(log n))
class Solution2:
    def searchInsert(self, nums, target: int) -> int:
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = start + (end - start) //2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                end = mid-1
            else:
                start = mid+1
        return start

# Linear Time (O(n)) Solution
class Solution3:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if(nums[i]>= target):
                return i
        return len(nums)

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    sol = Solution()
    print(sol.searchInsert(nums, target))
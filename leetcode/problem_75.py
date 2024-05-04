# Problem 75: Sort Colors (Medium): https://leetcode.com/problems/sort-colors/
# hint: We check for each element if it is 0 swap with start
# if it is 2 swap with end and if it is 1 do nothing
class Solution:
    def sortColors(self, nums):
        index = 0
        start = 0
        if(len(nums) < 2):
            return
        end = len(nums) -1
        while(index <= end and start < end):
            if(nums[index] == 0):
                nums[index] = nums[start]
                nums[start] = 0
                start +=1
                index+=1
            elif(nums[index] == 2):
                nums[index] = nums[end]
                nums[end] = 2
                end -= 1
            else:
                index += 1


if __name__ == "__main__":
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums) # [0,0,1,1,2,2]
    nums = [2,0,1]
    s.sortColors(nums)
    print(nums) # [0,1,2]
    nums = [0]
    s.sortColors(nums)
    print(nums) # [0]
    nums = [1]
    s.sortColors(nums)
    print(nums) # [1]

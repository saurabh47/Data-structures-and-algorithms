# Problem 189. Rotate Array (Easy): https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if( k == 0 or length == 1 or length == k ):
            return
        end = (length - k) % length # k
        begin = end
        while(end != begin -1):
            print(end)
            nums.append(nums[end])
            end += 1
            end = end % length
        nums.append(nums[end])
        i = 0
        while(i != length):
            del nums[0]
            i += 1

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)
    print(nums) # [5,6,7,1,2,3,4]
    nums = [-1,-100,3,99]
    k = 2
    Solution().rotate(nums, k)
    print(nums) # [3,99,-1,-100]
    nums = [1,2]
    k = 1
    Solution().rotate(nums, k)
    print(nums) # [2,1]
    nums = [1,2,3]
    k = 1
    Solution().rotate(nums, k)
    print(nums) # [3,1,2]
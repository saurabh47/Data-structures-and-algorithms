### Problem 2554. Maximum Number of Integers to Choose From a Range I
### tags: Array, Hash Table
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # 0: NC, 1: C, -1: Ban
        # [-1, 0, 0, 0, -1]
        nums = [0] * n
        for index in banned:
            if(index <= len(nums)):
                nums[index - 1] = -1
        s = 0
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            index = i + 1
            if(num == -1):
                continue
            if(s + index > maxSum):
                break
            s = s + index
            nums[i] = 1
            count += 1
        # print("nums = ", nums)
        return count
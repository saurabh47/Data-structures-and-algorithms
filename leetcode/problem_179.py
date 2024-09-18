### Problem 179. Largest Number
### tags: array, string, greedy, sorting
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if(x + y  > y + x):
                return -1
            else:
                return 1
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int(''.join(nums)))
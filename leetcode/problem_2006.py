### Problem 2006. Count Number of Pairs With Absolute Difference K
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        diffs = {}
        count = 0
        for i in range(len(nums)):
            d = nums[i] - k
            a = nums[i] + k
            if(d in diffs):
                count += diffs[d]
            if(a in diffs):
                count += diffs[a]

            if(nums[i] in diffs):
                diffs[nums[i]] += 1
            else:
                diffs[nums[i]] = 1
        return count
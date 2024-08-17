### Problem 974. Subarray Sums Divisible by K (Medium): https://leetcode.com/problems/subarray-sums-divisible-by-k/

### Tags: Array, Hash Table, Math
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_sum = {}
        rem = {0: 1}
        s = 0
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            s += num
            r = s % k
            if(r in rem):
                count += rem[r]
                rem[r] += 1
            else:
                rem[r] = 1

        return count
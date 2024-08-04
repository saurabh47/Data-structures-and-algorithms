### Problem 1508. Range Sum of Sorted Subarray Sums (Medium): https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

### Tags: Array, Sorting, Prefix Sum

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(len(nums)):
            sum_n = 0
            for j in range(i, len(nums)):
                sum_n += nums[j]
                arr.append(sum_n)
        # arr.extend(nums)
        arr.sort()
        print(arr)
        sum_n = 0
        for i in range(left-1, right):
            sum_n += arr[i]
        return sum_n % (pow(10, 9) + 7)
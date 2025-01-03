### Problem 303. Range Sum Query - Immutable (Easy)
### tags: prefix sum, array
class NumArray:

    def __init__(self, nums: List[int]):
        self.pref_sum = [nums[0]]
        self.arr = nums
        for i in range(1, len(nums)):
            self.pref_sum.append(self.pref_sum[i-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.pref_sum[right] - self.pref_sum[left] + self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
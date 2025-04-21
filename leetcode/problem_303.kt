/** 
 * Problem 303. Range Sum Query - Immutable (Easy) tags: Array, Prefix Sum 
 * tags: Array, Prefix Sum
 * */

class NumArray(nums: IntArray) {
    var nums: IntArray
    init {
        this.nums = nums
    }
    fun sumRange(left: Int, right: Int): Int {
        /** input: [-2,0,3,-5,2,-1] left, right output: */
        var sum = 0
        for (i in left..right) {
            sum += nums[i]
        }
        return sum
    }
}

/**
 * Your NumArray object will be instantiated and called as such: var obj = NumArray(nums) var
 * param_1 = obj.sumRange(left,right)
 */

// This is an optimized version of the above code
// It uses prefix sum to calculate the sum of the range in O(1) time
class NumArrayOptimized(nums: IntArray) {
    var nums: IntArray
    init {
        this.nums = nums
        for (i in 1..(nums.size - 1)) {
            nums[i] = nums[i] + nums[i - 1]
        }
    }
    fun sumRange(left: Int, right: Int): Int {
        /**
         * input: [-2, 0, 3, -5, 2, -1] left, right output: sum from left to right Example: [-2, -2,
         * 1, -4, -2, -3]
         */
        if (left <= 0) {
            return nums[right]
        }
        return nums[right] - nums[left - 1]
    }
}

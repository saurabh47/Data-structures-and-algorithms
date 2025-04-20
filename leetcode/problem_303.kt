/**
 * Problem 303. Range Sum Query - Immutable (Easy)
 * tags: Array, Prefix Sum
 */
class NumArray(nums: IntArray) {
    var nums: IntArray
    init{
        this.nums = nums
    }
    fun sumRange(left: Int, right: Int): Int {
        /**
         * input: [-2,0,3,-5,2,-1] left, right
         * output:
         */            
         var sum = 0
         for(i in left..right){
            sum += nums[i]
         }
         return sum
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
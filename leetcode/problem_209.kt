/***
 * Problem 209. Minimum Size Subarray Sum
 * tags: sliding window
 */
// time complexity: O(n)
// space complexity: O(1)
class Solution {
    fun minSubArrayLen(target: Int, nums: IntArray): Int {
        /**
         * given: nums, target
         * output: min sub arr length that sums target
         * 
         */
        var left = 0
        var sum = 0
        var result = nums.size + 1
        for(right in nums.indices){
            sum += nums[right]
            while(sum >= target){
                result = min(result, right - left + 1)
                sum -= nums[left]
                left++
            }
        }
        if(result == nums.size + 1){
            return 0
        }
        return result
    }
}
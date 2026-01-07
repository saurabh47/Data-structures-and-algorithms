/**
 * Problem 1920. Build Array from Permutation
 * tags: Array, Simulation
 */
class Solution {
    fun buildArray(nums: IntArray): IntArray {
        var result = IntArray(nums.size){0}
        for(i in nums.indices){
            result[i] = nums[nums[i]]
        }
        return result
    }
}
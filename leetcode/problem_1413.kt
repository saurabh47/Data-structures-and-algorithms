/**
 * Problem 1413. Minimum Value to Get Positive Step by Step Sum (Easy)
 * tags: Array, Prefix Sum
 */

 // time complexity: O(n)
// space complexity: O(1)
class Solution {
    fun minStartValue(nums: IntArray): Int {
        var s = 0
        var min_s = 0
        for(i in nums.indices){
            s += nums[i]
            if(s < min_s){
                min_s = s
            }
        }
        return 1 - min_s
    }
}
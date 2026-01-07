/**
 * Problem 724. Find Pivot Index (Easy)
 * tags: Array, Prefix Sum
 */
class Solution {
    fun pivotIndex(nums: IntArray): Int {
        /*
        * input: arr
        * output: pivot index
        * example: [1,7,3,6,5,6]
        * prefix: [1, 8, 11, 17, 22, 28]
        */
        var prefix: IntArray = IntArray(nums.size){0}
        for(i in nums.indices){
            if(i == 0){
                prefix[i] = nums[i]
            } else{
                prefix[i] = prefix[i - 1] + nums[i]
            }
        }
        for(i in prefix.indices){
            var leftSum = prefix[i] - nums[i]
            var rightSum = prefix.last() - prefix[i]
            if(leftSum == rightSum){
                return i
            }
        }
        return -1
    }
}
/**
 * 2149. Rearrange Array Elements by Sign
 * https://leetcode.com/problems/rearrange-array-elements-by-sign/
 * Difficulty: Medium
 * tags: Array, Two Pointers
 */

// // time complexity: O(n)
// // space complexity: O(n)
class Solution {
    fun rearrangeArray(nums: IntArray): IntArray {
        /**
         * input: arr of equal +ve & -ve nums
         * output: - arr with consecutive elements,
         *         - order preserved
         *         - starts with +ve
         * example: [-2, 3, 2, -12, 16, -4, -5, 8]
         *          [3, 2, 16, 8, -2, -12, -4 -5]
         * [3, -2, 2, -12, 16, -4, 8, -5]
         */
        var pos = mutableListOf<Int>()
        var neg = mutableListOf<Int>()
        for(i in nums){
            if(i > 0){
                pos.add(i)
            } else {
                neg.add(i)
            }
        }
        var i = 0
        var index = 0
        while(i < nums.size){
            nums[i] = pos[index]
            nums[i + 1] = neg[index]
            i += 2
            index += 1
        }
        return nums
    }
}

// Note: inplace solution is not possible because you will lose the relative order
// // of the elements. So, we need to use extra space.

// // time complexity: O(n)
// // space complexity: O(n)

class SolutionOptimized {
    fun rearrangeArray(nums: IntArray): IntArray {
        /**
         * input: arr of equal +ve & -ve nums
         * output: - arr with consecutive elements,
         *         - order preserved
         *         - starts with +ve
         * example: [-2, 3, 2, -12, 16, -4, -5, 8]
         *          [3, 2, 16, 8, -2, -12, -4 -5]
         * [3, -2, 2, -12, 16, -4, 8, -5]
         */
        var pos = 0
        var neg = 1
        var result = IntArray(nums.size){0}
        for(i in nums){
            if(i > 0){
                result[pos] = i
                pos += 2
            }else{
                result[neg] = i
                neg += 2
            }
        }
        return result
    }
}
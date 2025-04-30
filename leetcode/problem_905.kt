/**
 * Problem 905. Sort Array By Parity
 * tags: Array, Two Pointers
 */
class Solution {
    fun sortArrayByParity(nums: IntArray): IntArray {
        /*
         * input: arr
         * output: arr [even..., odd...]
         * example: [5, 3, 2, 1, 4, 7, 6, 9, 0, 8]
         * [5, 3, 2, 1, 4, 7, 6, 9, 0, 8] 
         * [2, 4, 6, 0, 8, 7, 5, 9, 1, 3] 
         */
        fun swap(x: Int, y:Int): Unit{
            var temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp
        }

        var start = 0
        var end = 0
        while(end < nums.size){
            if(nums[start].and(1) == 0){
                start++
                end = start
                continue
            }
            if(nums[end].and(1) == 1){
                end++
            } else {
                swap(start, end)
                start++
            }
        }
        return nums
    }
}
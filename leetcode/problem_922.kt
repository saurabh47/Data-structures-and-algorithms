/**
 * Problem 922. Sort Array By Parity II
 * tags: Array, Two Pointers
 */

 // time complexity: O(n)
 // space complexity: O(1)
class Solution {
    fun sortArrayByParityII(nums: IntArray): IntArray {
        /*
        * input: arr
        * output: arr [odd at odd, even at even]
        * example: [7, 2, 3, 1, 5, 6, 8, 10]
        * example: [2, 7, 6, 1, 8, 3, 10, 5]
        */
        fun swap(x:Int, y:Int): Unit{
            var temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp
        }

        var start = 0
        var end = 0
        while(end < nums.size){
            /// if even place even and odd place odd move forward
            if((start % 2 == 0 && nums[start] % 2 == 0) || (start % 2 != 0 && nums[start] % 2 != 0)){
                start++
                end = start
                continue
            }
            /// if even place odd and odd place even and x != y then swap
            if((start != end) && ((start % 2 == 0 && nums[end] % 2 == 0) || (start % 2 != 0 && nums[end] % 2 != 0))){
                swap(start, end)
                start++
                end = start
            }
            end ++
        }
        return nums
    }   
}
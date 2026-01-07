// Problem 1365. How Many Numbers Are Smaller Than the Current Number (Easy)
// tags: Array, Sorting 
class Solution {
    fun smallerNumbersThanCurrent(nums: IntArray): IntArray {
        /* input: [arri]
         * output: [counti] => count js less than i
         * Brute Force O(n2) i != j
        */
        var result = IntArray(nums.size)
        for(i in nums.indices){
            var count = 0
            for(j in nums.indices){
                if(i != j){
                    if(nums[j] < nums[i]){
                        count += 1
                    }
                }
            }
            result[i] = count
        }
        return result
    }
}
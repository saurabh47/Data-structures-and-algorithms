/**
 * Problem 2799. Count Complete Subarrays in an Array (Medium) tags: Array, Hash Table, Sliding
 * Window
 */

// time complexity: O(n^2)
// space complexity: O(n)
class Solution {
    fun countCompleteSubarrays(nums: IntArray): Int {
        /*
         * input: arr of int
         * output: number of distinct subarrays
         * keywords: distinct,  subarray,
         * example: [1, 3, 2, 4, 1, 5, 6]
         *
         */
        var arrMap = HashMap<Int, Int>()
        for (num in nums) {
            val value = arrMap.getOrDefault(num, 0) + 1
            arrMap.put(num, value)
        }
        var distinctCount = arrMap.size
        var result = 0
        for (i in nums.indices) {
            var subArrMap = HashMap<Int, Int>()
            var distinct = 0
            for (j in i until nums.size) {
                val value = subArrMap.getOrDefault(nums[j], 0) + 1
                if (!subArrMap.containsKey(nums[j])) {
                    distinct++
                }
                subArrMap.put(nums[j], value)
                if (distinct == distinctCount) {
                    result++
                }
            }
        }
        return result
    }
}

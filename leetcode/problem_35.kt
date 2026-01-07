/* Problem 35. Search Insert Position (Easy)
 *   tags: Array, Binary Search
 *
 *
 */

class Solution {
    fun searchInsert(nums: IntArray, target: Int): Int {
        /**
         * given: a sorted array input: arr output: if found return index
         * ```
         *         else return index to insert
         * ```
         * Time complexity : O(logn)
         */

        /*      1 3 5 6 9   t = 4
         *       0 1 2 3 4
         *       s = 0
         *       end = 4, mid = 0
         */

        var start = 0 // start = 2
        var end = nums.size - 1 // end = 1
        while (start <= end) { // true
            var mid = start + (end - start) / 2 // mid = 1
            if (nums[mid] == target) { // 3 == 4 false
                return mid
            } else if (nums[mid] < target) { // false
                start = mid + 1
            } else {
                end = mid - 1
            }
        }
        return start
    }
}

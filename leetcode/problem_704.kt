/* Problem 704. Binary Search (Easy)
 * tags: Array, Binary Search
 */
class Solution {
    fun search(nums: IntArray, target: Int): Int {
        /** given: search target in sorted array input: arr output: index of target or -1 */
        var start = 0
        var end = nums.size - 1
        while (start <= end) {
            var mid = start + (end - start) / 2
            if (nums[mid] == target) {
                return mid
            } else if (nums[mid] > target) {
                end = mid - 1
            } else {
                start = mid + 1
            }
        }
        return -1
    }
}

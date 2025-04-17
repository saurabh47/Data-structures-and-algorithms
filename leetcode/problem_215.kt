// Problem 215: Kth Largest Element in an Array
// tags: [Array, Divide and Conquer, Sorting, Heap (Priority Queue)]
class Solution {
    fun findKthLargest(nums: IntArray, k: Int): Int {
        /*
         * input: nums, n= 5
         * output: kth largest
         * Example: [1, 2, 3, 4, 2, 7, 6, 5 8, 10]
         *        [1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
         *        [1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
         */
        val minHeap = PriorityQueue<Int>()
        for (num in nums) {
            minHeap.add(num)
            if (minHeap.size > k) {
                minHeap.poll()
            }
        }
        return minHeap.poll()
    }
}

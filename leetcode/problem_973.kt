/**
 * Problem 973. K Closest Points to Origin
 * tags: [Array, Divide and Conquer, Sorting, Heap (Priority Queue)]
 * output: k closest points to origin
 * time complexity: O(nlog(k)) k <= n
 */
class Solution {
    fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> {
        /*
         * input: arr[arr]
         * output: arr[arr]
        */
        var priorityQ = PriorityQueue<Pair<IntArray, Double>>(compareBy {it.second})
        var result = Array(k) { IntArray(2) }
        for((x, y) in points){
            var distance = sqrt((x*x + y*y).toDouble())
            var pair = Pair<IntArray, Double>(intArrayOf(x,y), distance)
            priorityQ.add(pair)
        }
        var index = 0
        while(index < k){
            var pair  = priorityQ.poll()
            result[index] = pair.first
            index += 1
        }
        return result
    }
}
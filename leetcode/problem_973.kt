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


/**
 * 
 * Problem 347. Top K Frequent Elements
 * time complexity: O(n), space complexity: O(n)
 */
class OptimizedSolution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
         /*
          * input: nums, k
          * output: top k elements by freq 
         */
 
         var hashMap = HashMap<Int, Int>()
         // array index to represent the freq of elements
         //
         var array = MutableList<MutableList<Int>>(nums.size + 1){mutableListOf()}
         for(num in nums){
             var freq = hashMap.getOrDefault(num, 0)
             hashMap.put(num, freq + 1)
         }
         for((key, value) in hashMap){
             array[value].add(key);
         }
 
         var count = 0
         var result = IntArray(k)
         for(i in array.size - 1 downTo 0){
           for(elem in array[i]){
             if (count >= k) break
             result[count] = elem
             count += 1
           }
           if (count >= k) break
         }
         return result
     }
 }
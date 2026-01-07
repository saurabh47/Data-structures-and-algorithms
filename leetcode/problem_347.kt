/**
 * Problem 347. Top K Frequent Elements
 * tags: [Array, Hash Table, Sorting, Heap (Priority Queue)]
 * output: top k elements by freq
 */

class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        /*
         * input: nums, k
         * output: top k elements by freq 
        */

        var hashMap = HashMap<Int, Int>()
        var priorityQ = PriorityQueue<Pair<Int, Int>>(compareBy { it.second })
        for(num in nums){
            var freq = hashMap.getOrDefault(num, 0)
            hashMap.put(num, freq + 1)
        }
        for((key, value) in hashMap){
            priorityQ.add(Pair<Int, Int>(key, -value))
        }
        var count = 0
        var result = IntArray(k)
        while(count < k){
            var pair = priorityQ.poll()
            result[count] = pair.first
            count += 1
        }
        return result
    }
}
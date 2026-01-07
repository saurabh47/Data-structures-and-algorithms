/**
 * Problem 1046. Last Stone Weight
 * tags: Heap, Priority Queue
 */
class Solution {
    fun lastStoneWeight(stones: IntArray): Int {
     /**
      * input: arr of stones
      * output: Last stone remaining after smash
      * Example: [2,7,4,1,8,1]
      *           [1, 1, 2, 4, 7, 8]
      *           [1]
      */   
        val maxHeap = PriorityQueue<Int>(compareByDescending { it })
        for(stone in stones){
            maxHeap.add(stone)
        }
        while(maxHeap.size != 1){
            var x = maxHeap.poll()
            var y = maxHeap.poll()
            maxHeap.add(abs(x - y))
        }
        return maxHeap.poll()
    }
}
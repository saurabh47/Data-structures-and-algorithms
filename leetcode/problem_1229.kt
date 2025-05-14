/**
 * Problem 1229. Meeting Scheduler
 * tags: Array, Two Pointers
 * time complexity: O(nlogn + mlogm), where n is the length of slots1 and m is the length of slots2
 * space complexity: O(1)
 */
class Solution {
    fun minAvailableDuration(slots1: Array<IntArray>, slots2: Array<IntArray>, duration: Int): List<Int> {
        /*
        10                     60   
        ------------------------
          12       17 21    50
           --------    ------    
        */
        slots1.sortBy(){it[0]}
        slots2.sortBy(){it[0]}
        var result = IntArray(2)
        var i = 0
        var j = 0
        while(i < slots1.size && j < slots2.size){
          var start = maxOf(slots1[i][0],slots2[j][0])
          var end = minOf(slots1[i][1],slots2[j][1])
          if(end - start >= duration){
            result[0] = start;
            result[1] = start + duration
            return result.toList()
          }
          if(slots1[i][1] < slots2[j][1]){
            i++
          }else{
            j++
          }
        }
        return List<Int>(0){0};
    }
}
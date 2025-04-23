/**
 * Problem 1399. Count Largest Group
 * tags: math, simulation
 */
class Solution {
    fun countLargestGroup(n: Int): Int {
        var result:Int = 0
        var maxSize:Int = 0
        var hashMap = HashMap<Int,Int>()
        for(i in 1..n){
          var sum = digitSum(i)
          var value:Int = hashMap.getOrDefault(sum, 0) + 1;
          maxSize = maxOf(maxSize,value)
          hashMap.put(sum, value)
        }
        for(value in hashMap.values){
          if(value == maxSize){
            result++
          }
        }
        // println("hashMap= $hashMap result=$result")
        return result
    }

    fun digitSum(n:Int):Int{
      var s = 0
      var k = n;
      while(k != 0){
        var r = k % 10
        k = k / 10;
        s += r
      }
      return s;
    }
}
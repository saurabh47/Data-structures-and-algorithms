/**
 * Problem 875. Koko Eating Bananas (Medium)
 * tags: Binary Search
*/

// Brute Force O(n*m)
// n = size of piles and m = max of piles

class Solution {
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
       /**
        * input: arr of piles piles[i] is number of bananas in i
        *       h: number of hours 
        * output: return minimum eating speed k 
        * example: [3,6,7,11] 
        *           k = 1 = 27 hours > h
        *           k = 2 = 27 hours > h
        *           
        */ 
        var k = 1
        var maxOfPile:Long = piles.max().toLong()
        while(k < maxOfPile){
            var hours = hoursRequired(k, piles)
            if(hours <= h){
                break
            }
            k += 1
        }
        return k
    }

    fun hoursRequired(speed:Int,piles: IntArray): Long{
        var hours = 0L
        for(i in piles.indices){
            var pile = piles[i]
            var sp =  if (pile % speed == 0) pile / speed else (pile / speed) + 1
            hours += sp
        }
        return hours
    }
}


/**
 * Optimized Solution
 * Binary Search O(n*log(m))
 */

 class OptimizedSolution{
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
       /**
        * input: arr of piles piles[i] is number of bananas in i
        *       h: number of hours 
        * output: return minimum eating speed k 
        * example: [3,6,7,11] 
        *           k = 1 = 27 hours > h
        *           k = 2 = 27 hours > h
        *           
        */ 
        var start = 1L
        var end:Long = piles.max().toLong()
        while(start < end){
            var k = start + (end - start) / 2
            var hours = hoursRequired(k, piles)
            if(hours <= h){
                end = k
            } else {
                start = k + 1
            }
        }
        return start.toInt()
    }

    fun hoursRequired(speed:Long,piles: IntArray): Long{
        var hours = 0L
        for(i in piles.indices){
            var pile = piles[i].toLong()
            var sp =  if (pile % speed == 0L) pile / speed else (pile / speed) + 1
            hours += sp
        }
        return hours
    }
}
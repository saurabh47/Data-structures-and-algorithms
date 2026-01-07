/**
 * Problem 367. Valid Perfect Square (Easy)
 * tags: Binary Search
 */
class Solution {
    fun isPerfectSquare(num: Int): Boolean {
        /**
        * input: num
        * output: true/false
        * example:  n= 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1,4 ,15, 16
        */
        var start = 1L
        var end = num.toLong()
        while(start <= end){
            var mid: Long = start + (end - start) / 2
            var sqr: Long = mid * mid
            if(sqr == num.toLong()){
                return true
            } else if(sqr > num){
                end = mid - 1
            } else{
                start = mid + 1
            }
        }
        return false
    }
}
// Problem 1837. Sum of Digits in Base K (Easy)
// tags: math
// time complexity: O(log(n base k))

// space complexity: O(1)
class Solution {
    fun sumBase(n: Int, k: Int): Int {
        var result = 0
        var t = n
        while(t != 0){
            result += (t % k)
            t = t / k
        }
        return result
    }
}
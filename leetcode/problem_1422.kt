/**
 * Problem 1422. Maximum Score After Splitting a String
 * tags: greedy
 */
class Solution {
    fun maxScore(s: String): Int {
        var zero = 0
        var one = 0
        for(n in s) {
            if(n == '0'){
                zero++
            } else {
                one++
            }
        }
        var z = 0
        var o = 0
        var result = 0
        for(i in 0..(s.length - 2)) {
            var n = s[i]
            if(n == '0'){
                z++
            } else {
                o++
            }
            var sc = z + one - o
            if(sc > result){
                result = sc
            }
        }
        return result
    }
}
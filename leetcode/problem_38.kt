/**
 * Problem 38. Count and Say
 * tags: string
 */
class Solution {
    fun countAndSay(n: Int): String {
        var res = "1"
        for(i in 1 until n){
            res = runRLE(res)
        }
        return res
    }

    fun runRLE(s:String):String{
        var l = s.length
        // 1 2 1 1 
        var start = 0
        var count = 0
        var res = ""
        for(right in s.indices){
            if(s[right] == s[start]){
                count++
            }else{
                res += "$count${s[start]}"
                count = 1
                start = right
            }
        }
        res += "$count${s[start]}"
        return res
    }
}
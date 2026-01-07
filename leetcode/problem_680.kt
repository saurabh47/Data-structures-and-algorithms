// Problem 680. Valid Palindrome II (Easy)
// Tags: String, Two Pointers
class Solution {
    fun validPalindrome(s: String): Boolean {
        var start = 0 
        var end = s.length - 1
        var result = true 
        while(start < end){
            if(s[start] == s[end]){
                start += 1
                end -= 1
            } else{
                var ls = s.substring(start, end)
                var rs = s.substring(start + 1, end + 1)
                return ls.reversed() == ls || rs == rs.reversed()
            }
        }
        return result
    }
}
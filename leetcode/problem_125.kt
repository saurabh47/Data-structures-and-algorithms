// Problem 125. Valid Palindrome (Easy)
// Tags: String, Two Pointers

// O(n) time complexity
// O(1) space complexity
class Solution {
    fun isPalindrome(s: String): Boolean {
        fun isAlphaNumeric(index: Int):Boolean{
            val ascii = s[index].code
            if((ascii >= 97 && ascii <= 122) || (ascii >= 65 && ascii <= 90) || (ascii >= 48 && ascii <= 57)){
                return true
            }
            return false
        }

        var end = s.length - 1;
        var start = 0
        var result = true
        while(start < s.length){
            if(start > end || end < 0){
                break
            }
            if(!isAlphaNumeric(start)){
                start += 1
                continue
            }
           if(!isAlphaNumeric(end)){
                end -= 1
                continue
            }

            if(s[start].lowercaseChar() != s[end].lowercaseChar()){
                result = false
                break
            }
            end -= 1
            start += 1
        }
        return result
    }
}

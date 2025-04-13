// Problem 5. Longest Palindromic Substring
// tags: String, Two pointer Dynamic Programming

// time complexity: O(n^3)
// expands right
class Solution {
    fun longestPalindrome(s: String): String {
        /* given string
         * output: longest palindromic string
         * abcbasaabbcbbabcbbcbbaababac
         *
         */
        var result: String = ""
        var length = 0
        for (i in 0..s.length - 1) {
            for (j in i..s.length - 1) {
                var start = i
                var end = j
                var isPalindrome: Boolean = true
                while (start <= end) {
                    if (s[start] == s[end]) {
                        start += 1
                        end -= 1
                    } else {
                        isPalindrome = false
                        break
                    }
                }
                if (isPalindrome) {
                    if (j - i + 1 > length) {
                        result = s.substring(i, j + 1)
                        length = j - i + 1
                    }
                }
            }
        }
        return result
    }
}

// Slightly Optimized
// compresses the string
// time complexity: O(n^3)
class Solution {
    fun longestPalindrome(s: String): String {
        /* given string
         * output: longest palindromic string
         * abcbasaabbcbbabcbbcbbaababac
         *
         */
        var result: String = ""
        var length = 0
        for (i in 0..s.length - 1) {
            for (j in s.length - 1 downTo 0 step 1) {
                var start = i
                var end = j
                var isPalindrome: Boolean = true
                while (start <= end) {
                    if (s[start] == s[end]) {
                        start += 1
                        end -= 1
                    } else {
                        isPalindrome = false
                        break
                    }
                }
                if (isPalindrome) {
                    if (j - i + 1 > length) {
                        result = s.substring(i, j + 1)
                        length = j - i + 1
                    }
                    break
                }
            }
        }
        return result
    }
}


// Optimized solution
// time complexity: O(n^2)
// expand outward at each index to check if its a palindrome
// same as problem 647
class SolutionOptimized {
    fun longestPalindrome(s: String): String {
        /* given string
         * output: longest palindromic string
         * abcbasaabbcbbabcbbcbbaababac
         *
        */
        var result = ""
        var length = 0
        for(i in s.indices){
            var start = i
            var end = i
            var oddResult = longestPalindromicString(start, end, result, s)
            // even length palindrome
            start = i
            end = start + 1
            result = longestPalindromicString(start, end, oddResult, s)
        }
        return result
    }

    fun longestPalindromicString(i:Int, j: Int, res:String, s:String):String{
        var length = res.length
        var result = res
        var start = i
        var end = j
        while(start >= 0 && end < s.length && s[start] == s[end]){
            if(end - start + 1 > length){
                result = s.substring(start, end + 1)
                length = end - start + 1
            }
            start -= 1
            end += 1
        }
        return result
    }
}
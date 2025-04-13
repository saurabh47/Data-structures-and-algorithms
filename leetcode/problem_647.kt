// Problem 647. Palindromic Substrings
// tags: String, Dynamic Programming

// time complexity: O(n^3)
class Solution {
    fun countSubstrings(s: String): Int {
        /*
         * Given: a string
         * output: number of palindromic substrings
         *   a a a b b c c b b a a a
         *   0 1 2 3 4 5 6 7 8 9 10 11
         */
        var count = 0
        for (i in 0..s.length - 1) {
            for (j in i..s.length - 1) {
                var start = i
                var end = j
                var isPalindrome = true
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
                    count += 1
                }
            }
        }
        return count
    }
}

// Optimized solution
// time complexity: O(n^2)

class SolutionOptimized {
    fun countSubstrings(s: String): Int {
        /*
         * Given: a string
         * output: number of palindromic substrings
         *   a a a b b c c b b a a a
         *   0 1 2 3 4 5 6 7 8 9 10 11
         */
        var count = 0
        for (i in 0..s.length - 1) {
            var start = i
            var end = i
            //  check for odd length substrings expand outward
            while (start >= 0 && end < s.length && s[start] == s[end]) {
                if (s[start] == s[end]) {
                    start -= 1
                    end += 1
                    count += 1
                }
            }
            // check for even length palindromes
            start = i
            end = i + 1
            while (start >= 0 && end < s.length && s[start] == s[end]) {
                if (s[start] == s[end]) {
                    start -= 1
                    end += 1
                    count += 1
                }
            }
        }
        return count
    }
}

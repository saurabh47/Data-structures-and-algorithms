/*
* Problem 3. Longest Substring Without Repeating Characters (Medium) tags: Array, Hash Table, Sliding Window
* tags: Array, Hash Table, Sliding Window
*
*/
// time complexity: O(n)
// space complexity: O(n)
// hints: this is a snail technique expand on right side and shrink on left side
class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        /*
         * given: a string 
         * output: longest substring with unique chars
         * example: a b c b a d b c e a d b
         */

        var start = 0
        var end = 0
        var set = hashSetOf<Char>()
        var res = 0
        while(end < s.length){
            if(!set.contains(s[end])){
                set.add(s[end])
                res = maxOf(set.size, res)
                end += 1
                continue
            }
            while(s[start] != s[end]){
                set.remove(s[start])
                start+= 1
            }
            set.remove(s[start])
            start+= 1
        }
        return res
    }
}
// problem 408  Valid Word Abbreviation
// tag: String
class Solution {
    fun validWordAbbreviation(word: String, abbr: String): Boolean {
        fun isLetter(char: Char): Boolean {
            return (char.code >= 97 && char.code <= 122)
        }
        //   j
        // i n t e r n a t i o  n  a   l  i   z   a   t  i   o  n
        // 0 1 2 3 4 5 6 7 8 9 10  11 12  13  14  15 16  17 18 19
        // i        <12>                  i   z   <4>           n
        var i = 0
        var j = 0
        while (i < abbr.length && j < word.length) {
            if (abbr[i] != word[j]) {
                var number = ""
                while (i < abbr.length && !isLetter(abbr[i])) {
                    number += abbr[i]
                    i += 1
                }
                if (number.isEmpty() || number[0] == '0') {
                    return false
                }
                val num = number.toInt()
                j += num
            } else {
                i += 1
                j += 1
            }
        }
        if ((j != word.length) or (i != abbr.length)) {
            return false
        } else {
            return true
        }
    }
}

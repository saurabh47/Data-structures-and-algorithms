### Problem 1072. Flip Columns For Maximum Number of Equal Rows (Medium): https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

### tags: Array, Hash Table, Matrix
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def inverted(s):
            result = ''
            for letter in s:
                result += ('1' if letter == '0' else '0')
            return result

        lookUp = defaultdict(int)
        result = 0
        for row in matrix:
            k = ''
            for char in row:
                k += str(char)
            if(k[0] == '1'):
                k = inverted(k)
            lookUp[k] += 1
            result = max(result, lookUp[k])
        return result
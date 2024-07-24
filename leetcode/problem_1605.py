### Problem 1605. Find Valid Matrix Given Row and Column Sums (Medium): https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

### tags: greedy, matrix

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0 for j in range(len(colSum))] for i in range(len(rowSum))]
        for row in range(len(rowSum)):
            for col in range(len(colSum)):
                min_val = min(colSum[col], rowSum[row])
                result[row][col] = min_val
                rowSum[row] -= min_val
                colSum[col] -= min_val
        return result
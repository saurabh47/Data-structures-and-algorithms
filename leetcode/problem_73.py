### Problem 73. Set Matrix Zeroes
### Tags: Array, Hash Table

# Time Complexity: O(m*n)
# Space Complexity: O(max(m,n))

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        hmap = {}
        def zeroMxN(m:int, n:int)->None:
            for i in range(len(matrix[m])):
                matrix[m][i] = 0

            for i in range(len(matrix)):
                matrix[i][n] = 0


        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                elem = matrix[row][col]
                if(elem == 0):
                    hmap[(row, col)] = True

        for key, value in hmap.items():
            row, col = key
            zeroMxN(row, col)






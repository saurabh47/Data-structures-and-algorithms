### Problem 304. Range Sum Query 2D - Immutable (Medium)
### tags: prefix sum, matrix

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.pref_matrix = []
        for i in range(self.rows + 1):
            m = []
            for j in range(self.cols + 1):
                if(i == 0 or j == 0):
                    m.append(0)
                else:
                    m.append(matrix[i-1][j-1])
            self.pref_matrix.append(m)
        self.computePrefix()
        print("matrix=", self.pref_matrix)
# [   
#     [0, 0, 0, 0, 0, 0], 
#     [0, 3, 3, 1, 4, 2], 
#     [0, 5, 6, 3, 2, 1], 
#     [0, 1, 2, 0, 1, 5], 
#     [0, 4, 1, 0, 1, 7], 
#     [0, 1, 0, 3, 0, 5]
# ]

# [   
# [
    # [0, 0, 0, 0, 0, 0], 
    # [0, 3, 3, 4, 8, 10], 
    # [0, 8, 14, 18, 24, 27], 
    # [0, 9, 17, 21, 28, 36], 
    # [0, 13, 22, 26, 34, 49], 
    # [0, 14, 23, 30, 38, 58]]
#  ]

    def computePrefix(self):
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                curr = self.pref_matrix[i][j]
                prev = self.pref_matrix[i][j-1]
                above = self.pref_matrix[i - 1][j]
                diag_overlap = self.pref_matrix[i - 1][j - 1]
                self.pref_matrix[i][j] = curr + prev + above - diag_overlap

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        row2+=1
        col1+=1
        col2+=1
        top_row_sum = self.pref_matrix[row1 - 1][col2]
        top_col_sum = self.pref_matrix[row2][col1 - 1]
        overlapping_sum = self.pref_matrix[row1 - 1][col1 - 1]
        
        return self.pref_matrix[row2][col2] - top_row_sum - top_col_sum + overlapping_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
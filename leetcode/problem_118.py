### Problem 118. Pascal's Triangle (Easy): https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pt = [[1], [1, 1]]
        if(numRows == 1):
            return [pt[0]]
        for row in range(2, numRows):
            col = []
            for column in range(row+1): 
                if(column == 0 or column==row):
                    col.append(1)
                else:
                    col.append(pt[row-1][column -1] + pt[row-1][column])
            pt.append(col)
        return pt 
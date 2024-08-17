### Problem 119. Pascal's Triangle II (Easy): https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pt = [[1], [1, 1]]
        if(rowIndex < 2):
            return pt[rowIndex]
        for row in range(2, rowIndex + 1):
            column = []
            for col in range(row + 1):
                if(col == 0 or col == row):
                    column.append(1)
                else:
                    column.append(pt[row-1][col-1] + pt[row -1][col])
            pt.append(column)
        return pt[rowIndex]
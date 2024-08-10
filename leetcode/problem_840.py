class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isUnique(row, col):
            hm = {}
            isDistinct = True
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if(grid[r][c] not in hm and grid[r][c] >= 1 and grid[r][c] <= 9):
                        hm[grid[r][c]] = 1
                    else:
                        return False
            return True

        def isMagicSquare(row, col):
            if(not isUnique(row, col)):
                return False

            # check if sum in rows
            for r in range(row, row + 3):
                row_sum = sum(grid[r][col:col+3])
                # sum of 1..9 = 45 so each row/col in MS should sum 45/3 = 15
                print("row sum=",row_sum)
                if(row_sum != 15):
                    return False

            # check if sum in cols
            for c in range(col, col + 3):
                col_sum = grid[row][c] + grid[row+1][c] + grid[row + 2][c]
                print("col sum=",col_sum)
                if(col_sum != 15):
                    return False

            # check if sum in left diagonals
            ld_sum = 0

            for i in range(3):
                ld_sum += grid[row + i][col + i]

            print("ld sum=",ld_sum)
            if(ld_sum != 15):
                return False

            # check if sum in right diagonals
            rd_sum = 0
            for i in range(3):
                rd_sum += grid[row + i][col + 2 - i]

            print("rd sum=",rd_sum)
            if(rd_sum != 15):
                return False

            return True

        count = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                if(isMagicSquare(row, col)):
                    count += 1
        return count

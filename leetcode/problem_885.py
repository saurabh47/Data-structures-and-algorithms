### Problem 885. Spiral Matrix III
### Tags: Array, Matrix, Simulation
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        # E = 0, S = 1, W = 2, N = 3
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        direction = 0
        units = 1
        while(len(result) < rows * cols):
            for x in range(2):
                for step in range(units):
                    if(rStart>=0 and rStart<rows and cStart >=0 and cStart < cols):
                        result.append([rStart, cStart])
                    rStart += directions[direction][0] 
                    cStart += directions[direction][1]
                direction = (direction + 1) % 4
            units += 1
        return result

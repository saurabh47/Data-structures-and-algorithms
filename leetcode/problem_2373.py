class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid) - 2
        maxLocal = [[0 for i in range(m)] for i in range(m)]
        for i in range(m):
            for j in range(m):
                max_num = 0
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if(grid[k][l] > max_num):
                            max_num = grid[k][l]
                maxLocal[i][j] = max_num
        return maxLocal
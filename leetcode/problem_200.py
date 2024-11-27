### Problem 200. Number of Islands
### tags: Array, DFS, BFS, Matrix

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        def traverse_island(r, c):
            grid[r][c] = '0'
            # left
            if(c - 1 >= 0 and grid[r][c - 1] == '1'):
                traverse_island(r, c - 1)
            # down
            if(r + 1 < rows and grid[r + 1][c] == '1'):
                traverse_island(r + 1, c)
            # right
            if(c + 1 < cols and grid[r][c + 1] == '1'):
                traverse_island(r, c + 1)
            # top
            if(r - 1 >= 0 and grid[r - 1][c] == '1'):
                traverse_island(r - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                ch = grid[r][c]
                if(ch == '1'):
                    count += 1
                    traverse_island(r, c)
        return count
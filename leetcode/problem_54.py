### Problem 54.Spriral Matrix (Medium): https://leetcode.com/problems/spiral-matrix/
### tags: array, matrix, simulation

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #           R, B, L, T
        directions  = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result = []
        rows = len(matrix)
        cols = len(matrix[0])
        visited  = [[False for i in range(cols)] for j in range(rows)]
        direction = 0
        r, c = 0, 0
        if not matrix:
            return result

        for _ in range(rows * cols):
            result.append(matrix[r][c])
            visited[r][c] = True
            dr, dc = directions[direction]
            new_r, new_c = r + dr, c + dc
            # if out of bounds or visited
            if((new_r  >= rows) or (new_r < 0) or (new_c < 0) or (new_c >= cols) or (visited[new_r][new_c])):
                direction = (direction + 1) % 4
                dr, dc = directions[direction]
                new_r, new_c = r + dr, c + dc
            r , c = new_r, new_c
    
        return result
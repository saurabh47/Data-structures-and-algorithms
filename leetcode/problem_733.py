### Problem 733. Flood Fill (Easy): https://leetcode.com/problems/flood-fill/
### tags: Array, DFS, BFS, Matrix
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        if target == color:
            return image
            
        def fill(r, c):
            image[r][c] = color
            if(r - 1 >= 0 and image[r - 1][c] == target):
                fill(r - 1, c)
            if(r + 1 < rows and image[r + 1][c] == target):
                fill(r + 1, c)
            if(c - 1 >= 0 and image[r][c - 1] == target):
                fill(r, c - 1)
            if(c + 1 < cols and image[r][c + 1] == target):
                fill(r, c + 1)
        
        fill(sr, sc)
        return image
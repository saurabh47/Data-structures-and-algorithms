/**
 * Problem 733: Flood Fill
 * tags: DFS, BFS
 */

// time complexity: O(m*n)
// space complexity: O(1)

class Solution {
    fun floodFill(image: Array<IntArray>, sr: Int, sc: Int, color: Int): Array<IntArray> {
        /**
          * input: grid of image m x n
          * ouput: modified grid
          * call stack: [1, 1]
         */

        fun fillColor(row: Int, col: Int, target: Int): Unit{
            if(image[row][col] == color) return
            image[row][col] = color
             // go up
            if(row > 0 && image[row - 1][col] == target){
                fillColor(row - 1, col, target)
            }
            // go right
            if(col < image[0].size - 1 && image[row][col + 1] == target){
                fillColor(row, col + 1, target)
            }
            // go down
            if(row < image.size - 1 && image[row + 1][col] == target){
                fillColor(row + 1, col, target)
            }
            // go left
            if(col > 0 && image[row][col - 1] == target){
                fillColor(row, col - 1, target)
            }
        } 
        fillColor(sr, sc, image[sr][sc])
        return image         
    }
}
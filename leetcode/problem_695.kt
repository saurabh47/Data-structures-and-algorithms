/**
 * Problem 695. Max Area of Island
 * tags: DFS, BFS
 */

// time complexity: O(m*n)
// space complexity: O(m*n)
class Solution {
    fun maxAreaOfIsland(grid: Array<IntArray>): Int {
        var rows = grid.size
        var cols = grid[0].size
        var visited = mutableSetOf<Pair<Int, Int>>()
        
        fun islandTraversal(r: Int, c: Int, area: Int):Int{
            var pair = Pair<Int, Int>(r, c);
            if(visited.contains(pair)){
                return area
            }
            var newArea = area + 1
            visited.add(Pair<Int, Int>(r, c))
            // go top
            if(r > 0 && grid[r - 1][c] == 1){
                newArea = islandTraversal(r - 1, c, newArea)
            }
            // go right
            if(c  < cols - 1 && grid[r][c + 1] == 1){
                newArea = islandTraversal(r, c + 1, newArea)
            }
            // go down
            if(r < rows - 1 && grid[r + 1][c] == 1){
                newArea = islandTraversal(r + 1, c, newArea)
            }
            // go left
            if(c > 0 && grid[r][c - 1] == 1){
                newArea = islandTraversal(r, c - 1, newArea)
            }
            return newArea
        }

        var  result = 0
        for(i in 0..(rows - 1)){
            for(j in 0..(cols - 1)){
                if(!visited.contains(Pair<Int, Int>(i,j)) && grid[i][j] == 1){
                    var area = islandTraversal(i, j, 0)
                    result = maxOf(result, area)
                }
            }
        }
        return result
    }
}

// time complexity: O(m*n)
// space complexity: O(1)
class OptimizedSolution {
    fun maxAreaOfIsland(grid: Array<IntArray>): Int {
        var rows = grid.size
        var cols = grid[0].size
        
        fun islandTraversal(r: Int, c: Int, area: Int):Int{
            grid[r][c] = 0
            var newArea = area + 1
            // go top
            if(r > 0 && grid[r - 1][c] == 1){
                newArea = islandTraversal(r - 1, c, newArea)
            }
            // go right
            if(c  < cols - 1 && grid[r][c + 1] == 1){
                newArea = islandTraversal(r, c + 1, newArea)
            }
            // go down
            if(r < rows - 1 && grid[r + 1][c] == 1){
                newArea = islandTraversal(r + 1, c, newArea)
            }
            // go left
            if(c > 0 && grid[r][c - 1] == 1){
                newArea = islandTraversal(r, c - 1, newArea)
            }
            return newArea
        }

        var  result = 0
        for(i in 0..(rows - 1)){
            for(j in 0..(cols - 1)){
                if(grid[i][j] == 1){
                    var area = islandTraversal(i, j, 0)
                    result = maxOf(result, area)
                }
            }
        }
        return result
    }
}
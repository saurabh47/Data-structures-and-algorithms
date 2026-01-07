/** Problem 200. Number of Islands tags: DFS, BFS */

// time complexity: O(m*n)
// space complexity: O(m*n)
operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>): Pair<Int, Int> =
        Pair(this.first + other.first, this.second + other.second)

class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        var directions =
                arrayOf<Pair<Int, Int>>(
                        Pair<Int, Int>(0, -1),
                        Pair<Int, Int>(1, 0),
                        Pair<Int, Int>(0, 1),
                        Pair<Int, Int>(-1, 0),
                )
        val visited = mutableSetOf<Pair<Int, Int>>()
        /*
         * input: grid mxn
         * output: number of islands
         *
         */
        fun dfs(pair: Pair<Int, Int>): Unit {
            if (visited.contains(pair)) {
                return
            }
            visited.add(pair)
            var (row, col) = pair
            // go right
            if ((col < grid[0].size - 1) && grid[row][col + 1] == '1') {
                dfs(pair + directions[2])
            }
            // go down
            if (row < grid.size - 1 && grid[row + 1][col] == '1') {
                dfs(pair + directions[1])
            }
            // go left
            if (col > 0 && grid[row][col - 1] == '1') {
                dfs(pair + directions[0])
            }
            // go up
            if (row > 0 && grid[row - 1][col] == '1') {
                dfs(pair + directions[3])
            }
        }

        var islands = 0
        for (row in grid.indices) {
            for (col in grid[row].indices) {
                var pair = Pair(row, col)
                if (grid[row][col] == '1' && !visited.contains(pair)) {
                    islands++
                    dfs(pair)
                }
            }
        }
        return islands
    }
}


/**
 * 
 * Optimized DFS
 */

 // time complexity: O(m*n)
// space complexity: O(1)
 class OptimizedSolution {
    fun numIslands(grid: Array<CharArray>): Int {
        /*
         * input: grid mxn
         * output: number of islands
         *       ["0","0","0","0","0"],
                 ["0","0","0","0","0"],
                 ["0","0","1","0","0"],
                 ["0","0","0","1","1"]
         *
         */
        fun dfs(row: Int, col: Int): Unit{
            grid[row][col] ='0'
            // go right
            if((col < grid[0].size - 1) && grid[row][col + 1] == '1'){
               dfs(row, col + 1)
            }
            // go down
            if(row < grid.size - 1 && grid[row + 1][col] == '1'){
               dfs(row + 1, col)
            }
            // go left
            if(col > 0 && grid[row][col - 1] == '1'){
                dfs(row, col - 1)
            }
            // go up
            if(row > 0 && grid[row - 1][col] == '1'){
                dfs(row - 1, col)
            }
        }

        var islands = 0
        for(row in grid.indices){
            for(col in grid[row].indices){
                if(grid[row][col] == '1'){
                    islands++
                    dfs(row, col)
                }
            }
        }
        return islands
    }
}
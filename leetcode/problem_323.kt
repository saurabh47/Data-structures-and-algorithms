/**
 * Problem 323. Number of Connected Components in an Undirected Graph (Medium)
 * https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
 * tags: graph, depth-first search
 * time complexity: O(V + E), where V is the number of vertices and E is the number of edges
 */
class Solution {
    fun countComponents(n: Int, edges: Array<IntArray>): Int {
        var visited = HashSet<Int>()
        var adj = hashMapOf<Int, MutableList<Int>>()

        fun dfs(node: Int):Unit{
          if(visited.contains(node)) return
          visited.add(node)
          for(neighbor in adj.getOrDefault(node, mutableListOf<Int>())){
            if(!visited.contains(neighbor)){
                dfs(neighbor)
            }
          }
        }

        for(edge in edges){
          adj.getOrPut(edge[0]) { mutableListOf<Int>()}.add(edge[1])
          adj.getOrPut(edge[1]) { mutableListOf<Int>()}.add(edge[0])
        }
        var components = 0
        for(i in 0..(n-1)){
          if(!visited.contains(i)){
            components++
            dfs(i)
          }
        }
        return components
    }
}
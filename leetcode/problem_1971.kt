/**
 * Problem 1971. Find if Path Exists in Graph
 * tags: Graph, BFS
 * time complexity: O(n + m) where n is the number of nodes and m is the number of edges
 * space complexity: O(n + m) where n is the number of nodes and m is the number of edges
 */
class Solution {
    fun validPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
        var visited = HashSet<Int>()
        var adjList = HashMap<Int, MutableList<Int>>()
        val queue = ArrayDeque<Int>()

        // generate adjacency list
        for((start, end) in edges){
            if(!adjList.containsKey(start)){
                adjList.put(start, mutableListOf<Int>())
            }
            if(!adjList.containsKey(end)){
                adjList.put(end, mutableListOf<Int>())
            }
            adjList[start]?.add(end)
            adjList[end]?.add(start)
        }

        visited.add(source)
        queue.add(source)
        while(queue.size != 0){
            var target = queue.removeFirst()
            for(neighbor in adjList.getOrDefault(target, mutableListOf<Int>())){
                if(!visited.contains(neighbor)){
                    queue.add(neighbor)
                    visited.add(neighbor)
                }
            }
            if(target == destination){
                return true
            }
        }
        return false
    }
}
import java.io.*
import java.util.*

// time complexity: O(V + E)
// space complexity: O(V + E)
class Solution {
    fun cycle(edges: Array<IntArray>, source: Int): Boolean {

        var visited: HashSet<Int> = HashSet<Int>()
        var adj: HashMap<Int, MutableList<Int>> = HashMap<Int, MutableList<Int>>()

        /*      0-------1----4        5
         *      |       |   /         |
         *      |       |  /          |
         *      2-------3/            6-------7
         */
        //            2             3
        fun dfsHelper(source: Int, parent: Int): Boolean {
            if (visited.contains(source)) {
                return false
            }
            print("$source->")
            visited.add(source)
            var neighbors = adj.getOrDefault(source, mutableListOf<Int>())
            // 2: 0, 3,  p = 3
            for (neighbor in neighbors) {
                // 2: 0, 3  p = 1
                if (visited.contains(neighbor) && neighbor != parent) {
                    println("loop detected at $source: $neighbor $parent")
                    return true
                }
                if (dfsHelper(neighbor, source)) {
                    return true
                }
            }
            return false
        }

        for (edge in edges) {
            var (start, end) = edge
            if (!adj.containsKey(start)) {
                adj.put(start, mutableListOf<Int>())
            }
            if (!adj.containsKey(end)) {
                adj.put(end, mutableListOf<Int>())
            }
            adj[start]?.add(end)
            adj[end]?.add(start)
        }
        // any value that is not in graph
        var parent = -1
        println("adj list= $adj")
        for (node in adj.keys) {
            if (!visited.contains(node)) {
                var cycle = dfsHelper(node, parent)
                if (cycle == true) {
                    return true
                }
            }
        }
        return false
    }
}

fun main() {
    var solution = Solution()
    var edges =
            arrayOf<IntArray>(
                    intArrayOf(0, 1),
                    intArrayOf(2, 3),
                    intArrayOf(0, 2),
                    intArrayOf(1, 3),
                    intArrayOf(1, 4),
                    intArrayOf(3, 4),
                    intArrayOf(5, 6),
                    intArrayOf(6, 7)
            )

    /*      0-------1----4        5
     *      |       |   /         |
     *      |       |  /          |
     *      2-------3/            6-------7
     */

    var source = 0
    println(solution.cycle(edges, source))
}

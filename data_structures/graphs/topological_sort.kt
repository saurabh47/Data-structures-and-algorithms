import java.io.*
import java.util.*

class Solution {
    fun topologicalSort(edges: Array<IntArray>): List<Int> {
        val adj = HashMap<Int, MutableList<Int>>()
        var indegree = mutableMapOf<Int, Int>()
        val result = mutableListOf<Int>()
        for (edge in edges) {
            var (u: Int, v: Int) = edge
            adj.getOrPut(u) { mutableListOf() }.add(v)
            indegree[v] = indegree.getOrDefault(v, 0) + 1
            indegree[u] = indegree.getOrDefault(u, 0)
        }

        val q = ArrayDeque<Int>()
        for ((node, degree) in indegree) {
            if (degree == 0) {
                q.add(node)
            }
        }
        while (q.isNotEmpty()) {
            val top = q.removeFirst()
            result.add(top)
            val neighbors = adj.getOrDefault(top, mutableListOf<Int>())
            for (neighbor in neighbors) {
                indegree[neighbor] = indegree.getOrDefault(neighbor, 0) - 1
                if (indegree[neighbor] == 0) {
                    q.add(neighbor)
                }
            }
        }

        return result
    }
}

fun main() {
    var solution = Solution()
    var edges =
            arrayOf<IntArray>(
                    intArrayOf(0, 1),
                    intArrayOf(0, 2),
                    intArrayOf(1, 3),
                    intArrayOf(1, 4),
                    intArrayOf(4, 3),
                    intArrayOf(2, 3),
                    intArrayOf(5, 6),
                    intArrayOf(6, 7)
            )

    /*      0------>1---->4        5
     *      |       |    /         |
     *      v       v  /           v
     *      2------>3<-            6------>7
     */

    println("topologicalSort=${solution.topologicalSort(edges).contentToString()}")
}

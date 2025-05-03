/** Problem 997. Find the Town Judge tags: Graph, BFS */
// time complexity: O(n + m) where n is the number of nodes and m is the number of edges
// space complexity: O(n + m) where n is the number of nodes and m is the number of edges
class Solution {
    fun findJudge(n: Int, trust: Array<IntArray>): Int {
        /*
         * input: trust [[ai, bi]] ai -> bi, n= [1, n]
         * output: x: int = towm judget, otherwise -1
         * example: n= 5
         * trust = [[2, 3], [1, 4], [1, 3], [4, 3], [5, 3]]
         */
        var judge = -1
        var trustScore: HashMap<Int, Int> = HashMap<Int, Int>()
        if (n == 1) {
            return n
        }
        for ((i, j) in trust) {
            val score = trustScore.getOrDefault(i, 0) - 1
            val tscore = trustScore.getOrDefault(j, 0) + 1
            trustScore.put(i, score)
            trustScore.put(j, tscore)
        }
        for ((i, j) in trustScore) {
            if (j == (n - 1)) {
                judge = i
                break
            }
        }
        return judge
    }
}

/** 
 * Optimized on memory usage 
 * time complexity: O(n + m) where n is the number of nodes and m is the number of edges
 * space complexity: O(n) where n is the number of nodes
 * */

class OptimizedSolution {
    fun findJudge(n: Int, trust: Array<IntArray>): Int {
        var judge = -1
        if (n == 1) {
            return 1
        }
        var trustScore = IntArray(n + 1) { 0 }
        for ((i, j) in trust) {
            trustScore[i]--
            trustScore[j]++
        }
        for (i in trustScore.indices) {
            if (trustScore[i] == (n - 1)) {
                judge = i
                break
            }
        }
        return judge
    }
}

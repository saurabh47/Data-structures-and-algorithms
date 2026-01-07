/**
 * Problem 199. Binary Tree Right Side View
 * tags: Tree, Depth-First Search, Breadth-First Search
 * time complexity: O(n)
 * space complexity: O(w), because we are using a queue to store the nodes at the current level
 * where w is the maximum width of the tree
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun rightSideView(root: TreeNode?): List<Int> {
        if(root == null){
            return emptyList()
        }
        var q = ArrayDeque<TreeNode>()
        q.add(root)
        var result = mutableListOf<Int>()
        while(true){
            var size = q.size
            if(size == 0){
                break
            }
            var last = -1
            while(size != 0){
                var top = q.removeFirst()
                if(size == 1){
                    last = top.`val`
                }
                if(top.left != null){
                    q.add(top.left)
                }
                if(top.right != null){
                    q.add(top.right)
                }
                size -= 1
            }
            result.add(last)
        }
        return result
    }
}

/**
 * DFS solution
 * tags: Tree, Depth-First Search
 * time complexity: O(n)
 * space complexity: O(h), where h is the height of the tree
 */

class Solution {
    fun rightSideView(root: TreeNode?): List<Int> {
        var result = mutableListOf<Int>()
        if(root == null){
            return emptyList()
        }
        fun dfsHelper(node: TreeNode?, level: Int): Unit{
            if(node == null) return 
            if(result.size == level) result.add(node.`val`)
            dfsHelper(node.right, level+1)
            dfsHelper(node.left, level+1)
        }

        dfsHelper(root, 0)
        return result
    }
}
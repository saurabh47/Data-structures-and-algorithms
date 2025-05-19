/**
 * Problem 124. Binary Tree Maximum Path Sum
 * tags: tree, depth-first-search
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
    fun maxPathSum(root: TreeNode?): Int {
        var maxSum = Int.MIN_VALUE
        fun pathSum(node: TreeNode?): Int{
            if(node == null) return 0

            var left = maxOf(0, pathSum(node.left))
            var right = maxOf(0, pathSum(node.right))

            var pathSumMid = left  + right + node.`val`
            maxSum = maxOf(pathSumMid, maxSum)
            return node.`val` + maxOf(left, right)
        }
        var res = pathSum(root)
        return maxSum
    }
}
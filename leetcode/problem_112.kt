/**
 * Problem 112. Path Sum (Easy)
 * https://leetcode.com/problems/path-sum/
 * tags: Tree, Depth-first Search
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
    fun hasPathSum(root: TreeNode?, targetSum: Int): Boolean {
        fun dfs(node: TreeNode?, curr: Int):Boolean{
            if(node == null){
                return false
            }
            if(node.left == null && node.right == null){
                if(curr + node.`val` == targetSum){
                    return true
                }
            }
            var left = dfs(node.left, curr + node.`val`)
            if(left == true){ 
                return true
            }
            var right = dfs(node.right, curr + node.`val`)
            if(right == true){ 
                return true
            }
            return false
        }
        return dfs(root, 0)
    }
}
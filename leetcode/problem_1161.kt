
/**
 * Problem 1161. Maximum Level Sum of a Binary Tree (Medium)
 * tags: Tree, Depth-first Search, Breadth-first Search
 * time complexity: O(n) 
 * space complexity: O(n)
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
    fun maxLevelSum(root: TreeNode?): Int {
        var q = ArrayDeque<TreeNode>()
        if(root != null){
            q.add(root)
        }
        var maxSum = -100000
        var result = 1
        var level = 0;
        while(true){
            var size = q.size;
            var levelSum = 0
            if(size == 0){
                break
            }
            while(size != 0){
                var top = q.removeFirst()
                levelSum += top.`val`
                if(top.left != null){
                    q.add(top.left)
                }
                if(top.right != null){
                    q.add(top.right)
                }
                size -= 1
            }
            level++
            if(levelSum > maxSum){
                result = level
                maxSum = levelSum
            }
        }
        return result
    }
}
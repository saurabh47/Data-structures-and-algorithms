// Problem 102. Binary Tree Level Order Traversal
// tags: Medium, Tree, BFS

class Solution {
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        val result: MutableList<MutableList<Int>> = mutableListOf()
        fun levelTrav(node: TreeNode?, level:Int){
            if(node == null) return
            if(result.size == level){
                result.add(mutableListOf<Int>())
            }
            result[level].add(node!!.`val`)
            if(node.`left` != null){
                levelTrav(node.`left`, level + 1)
            }
            if(node.`right`!= null){
                levelTrav(node.`right`, level + 1)
            }
        }

        levelTrav(root, 0)
        return result
    }
}
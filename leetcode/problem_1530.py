### Problem 1530. Number of Good Leaf Nodes Pairs (Medium): https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

### tags: binary tree, dfs, recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        def dfs(node: TreeNode):
            if(node is None):
                return []
            if(node.left is None and node.right is None):
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for l in left:
                for r in right:
                    if(l + r <= distance):
                        self.count += 1
            left.extend(right)
            left = [num + 1 for num in left]
            return left
            
        distances = dfs(root)
        return self.count
      
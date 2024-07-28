### Problem 257. Binary Tree Paths (Easy): https://leetcode.com/problems/binary-tree-paths/

### Tags: Tree, Depth First Search, Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.result = []
        def paths(root, path):
            if(root is None):
                return []
            if(len(path) == 0):
                path += str(root.val)
            else:
                path += ('->' + str(root.val))
            if(not root.left and not root.right):
                self.result.append(path)
            if(root.left):
                paths(root.left,path)
            if(root.right):
                paths(root.right,path)

        paths(root, "")
        return self.result
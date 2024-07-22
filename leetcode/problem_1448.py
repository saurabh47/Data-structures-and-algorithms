# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # paths: 3 : good
        # paths: 3 -> 1 : false
        # paths: 3 -> 1 -> 3 : good
        # paths: 3 -> 4: good
        # paths: 3 -> 4 -> 1 : false
        # paths: 3 -> 4 -> 5 : good
        def isGood(node, max_val):
            if(node is None):
                return 0
            count = 0
            if(node.val >= max_val):
                count = 1
                max_val = node.val
            count += isGood(node.left, max_val)
            count += isGood(node.right, max_val)
            return count

        return isGood(root, root.val)
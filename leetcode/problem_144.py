### Problem 144. Binary Tree Preorder Traversal (Medium): https://leetcode.com/problems/binary-tree-preorder-traversal/

### Tags: Tree, Depth First Search, Stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preOrder(root: Optional[TreeNode]):
            if(root is None):
                return
            order.append(root.val)
            preOrder(root.left)
            preOrder(root.right)

        order = []
        preOrder(root)
        return order

### Iteration

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if(root is None):
            return result
        stack = []
        while(True):
            while(root):
                stack.append(root)
                result.append(root.val)
                root = root.left
            if(not stack):
                break
            root = stack.pop()
            root = root.right
        return result
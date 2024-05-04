# Problem 94. Binary Tree Inorder Traversal (Medium)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while(True):
            while(root):
                stack.append(root)
                root = root.left
            if(not stack):
                break
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result 
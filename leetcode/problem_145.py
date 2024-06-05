### Problem 145. Binary Tree Postorder Traversal (Hard): https://leetcode.com/problems/binary-tree-postorder-traversal/

### Tags: Tree, Depth First Search, Stack
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
### Problem 783. Minimum Distance Between BST Nodes
### Tags: Tree, Depth First Search, Binary Search Tree

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = []
        stack = []
        while(True):
            while(root):
                stack.append(root)
                root = root.left
            if(not stack):
                break
            root = stack.pop()
            result.append(root.val)
            root = root.right
        min_val = 100000
        for i in range(1, len(result)):
            curr = result[i]
            prev = result[i - 1]
            if(abs(curr - prev) < min_val):
                min_val = abs(curr - prev)
        return min_val
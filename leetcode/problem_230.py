### Problem 230. Kth Smallest Element in a BST (Medium)
### Tags: Binary Search Tree, Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []
        while(True):
            while(root):
                stack.append(root)
                root = root.left
            if(not stack):
                break
            root = stack.pop()
            count += 1
            if(count == k):
                return root.val
            root = root.right
        return -1


### Recursive Solution
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kthTraversal(root):
            if root is None:
                return None
            left = kthTraversal(root.left)
            if left is not None:
                return left
            self.count += 1
            if self.count == k:
                return root.val
            return kthTraversal(root.right)

        self.count = 0
        return kthTraversal(root)
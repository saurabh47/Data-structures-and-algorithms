### Problem 700. Search in a Binary Search Tree (Easy)

### Tags: Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while(root):
            if(root.val > val):
                root = root.left
            elif(root.val < val):
                root = root.right
            else:
                return root
        return root
### Problem 701. Insert into a Binary Search Tree (Medium): https://leetcode.com/problems/insert-into-a-binary-search-tree/

### tags: binary search tree, tree, recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insertBST(root):
            if(not root):
                return TreeNode(val)
            elif(not root.left and not root.right):
                if(root.val > val):
                    root.left = TreeNode(val)
                else:
                    root.right = TreeNode(val)
            else:
                if(root.val > val):
                    if(not root.left):
                        root.left = TreeNode(val)
                    else:
                        insertBST(root.left)
                else:
                    if(not root.right):
                        root.right = TreeNode(val)
                    else:
                        insertBST(root.right)

        if root:
            insertBST(root) 
            return root
        else:
            return TreeNode(val)
### Problem 404. Sum of Left Leaves (Easy): https://leetcode.com/problems/sum-of-left-leaves/
### Tags: Tree, Depth First Search, Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_left(root, sum_n, isLeft):
            if(root is None):
                return 0 
            if(root.left is None and root.right is None):
                if(isLeft):
                    sum_n += root.val
                    return sum_n
                else:
                    return 0
            left_sum = sum_left(root.left, sum_n, True) 
            right_sum = sum_left(root.right, sum_n, False)
            return left_sum + right_sum
        return sum_left(root, 0, False) 
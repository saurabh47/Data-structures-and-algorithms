### Problem 101. Symmetric Tree (Easy)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        return self.isSymmetricHelper(p,q)

    def isSymmetricHelper(self, left: TreeNode, right: TreeNode):
        if((left and not right) or (right and not left)):
            return False
        if(not right and not left):
            return True
        if(left.val != right.val):
            return False
        return  self.isSymmetricHelper(left.left,right.right) and self.isSymmetricHelper(left.right,right.left)

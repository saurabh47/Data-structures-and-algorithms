### Problem 100. Same Tree (Easy)

### Iterative solution
class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
        while(True):
            if(not self.same(p,q)):
                return False
            while(p and q):
                stack1.append(p)
                stack2.append(q)
                p = p.left
                q = q.left
                if(not self.same(p,q)):
                    return False
            if(not stack1 and not stack2):
                break
            if(not self.same(p,q)):
                return False
            p = stack1.pop()
            q = stack2.pop()
            p = p.right
            q = q.right
        return True

    def same(self, p: TreeNode, q: TreeNode) -> bool:
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True
        return p.val == q.val

### Recursive solution
class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### Recursive solution
# Check if preorder and inorder of both trees are same
class Solution3:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        inorder_p = []
        inorder_q = []
        preorder_p = []
        preorder_q = []

        def inorder(res,root: Optional[TreeNode]):
            if(root is None):
                res.append(100000)
                return
            inorder(res, root.left)
            res.append(root.val)
            inorder(res, root.right)
        
        def preOrder(res,root: Optional[TreeNode]):
            if(root is None):
                res.append(100000)
                return
            res.append(root.val)
            preOrder(res, root.left)
            preOrder(res, root.right)
        
        inorder(inorder_p, p)
        inorder(inorder_q, q)
        print("inorder:", inorder_p, inorder_q)
        if(len(inorder_p)!= len(inorder_q)):
            return False

        for i in range(len(inorder_p)):
            if(inorder_p[i] != inorder_q[i]):
                return False

        preOrder(preorder_p, p)
        preOrder(preorder_q, q)
        print("preorder:", preorder_p, preorder_q)
        if(len(inorder_p)!= len(inorder_q) or len(preorder_p)!= len(preorder_q) ):
            return False

        for i in range(len(inorder_p)):
            if(inorder_p[i] != inorder_q[i] or preorder_p[i] != preorder_q[i]):
                return False
        return True
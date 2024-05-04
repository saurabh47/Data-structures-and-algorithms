### Problem 100. Same Tree (Easy)
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
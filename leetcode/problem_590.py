### Problem 590. N-ary Tree Postorder Traversal (Easy): https://leetcode.com/problems/n-ary-tree-postorder-traversal/
### tags: tree, easy
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = []
        result = []
        if(root is None):
            return result
        stack.append(root)
        while(stack):
            root = stack.pop()
            result.append(root.val)
            for child in root.children:
                stack.append(child)
        return result[::-1]

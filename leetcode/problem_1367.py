### Problem 1367: Linked List in Binary Tree
### Difficulty: Medium
### tags: [Linked List, Tree, Depth First Search]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def isSame(l_head, troot):
            if(not l_head):
                return True
            elif(not troot or l_head.val != troot.val):
                return False
            elif(l_head.val == troot.val):
                return isSame(l_head.next, troot.left) or isSame(l_head.next, troot.right)
            else:
                return False
        if(isSame(head, root)):
            return True
        if(not root):
            return False
        return (self.isSubPath(head, root.left) or self.isSubPath(head, root.right))

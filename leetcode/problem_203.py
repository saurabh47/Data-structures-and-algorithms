### Problem 203. Remove Linked List Elements (Easy): https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        prev = None
        while(current):
            if(current.val == val):
                if(prev == None):
                    current = current.next
                    head = current
                else:
                    prev.next = current.next
                    current = current.next
            else:
                prev = current
                current = current.next
        return head

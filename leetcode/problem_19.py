### Problem 19. Remove Nth Node From End of List (Medium): https://leetcode.com/problems/remove-nth-node-from-end-of-list/

### tags: linked-list, two pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        if((current is None) or (current.next is None)):
            return None
        length = 0
        while(current):
            length += 1
            current = current.next
        current = head
        # print("len=", length)
        prev = None
        if(length == n):
            return current.next
        while(length != n):
            length -= 1
            prev = current
            current = current.next
        # print("toRemove", current.val)
        prev.next = current.next
        return head
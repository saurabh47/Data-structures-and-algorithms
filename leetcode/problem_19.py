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

# Single Pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        targetNode = head
        # give a head start to current
        for i in range(n):
            current = current.next

        # when n == len of list,
        # current reaches end, we are supposed to delete head
        if(current is None):
            return head.next
        # when current reaches end
        # target reaches at n
        while(current.next):
            targetNode = targetNode.next
            current = current.next

        # delete the node
        targetNode.next = targetNode.next.next
        return head

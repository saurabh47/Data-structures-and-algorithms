#### Problem 61. Rotate List (Medium)
#### Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_length = 0
        curr = head
        while(curr):
            list_length += 1
            curr = curr.next
        if(list_length == 0):
            return head
        if(k % list_length == 0):
            return head
        t = k % list_length
        # append last t elements to beginning of list
        curr = head
        prev = None
        count = 0
        while(count != list_length - t):
            count += 1
            prev = curr
            curr = curr.next
        prev.next = None

        new_head = curr
        while(curr.next):
            curr = curr.next
        curr.next = head
        return new_head        


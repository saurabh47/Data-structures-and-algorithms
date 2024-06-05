### Problem 24. Swap Nodes in Pairs

### Tags: Linked List, Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        current = head
        count = 0
        prev = None
        while(current):
            if(count % 2 == 0):
                # delete a node
                temp = current
                if(count == 0):
                    # delete at head
                    if(current.next):
                        head = current.next
                    prev = current
                    current = current.next
                else:
                    if(current.next):
                        prev.next = current.next
                    current = current.next
            else:
                temp.next = current.next
                current.next = temp
                prev = current.next
                if(current.next):
                    current = current.next.next
            count += 1
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def kthNode(current, k):
            while(current and k > 0):
                current = current.next
                k-= 1
            return current

        dummy = ListNode(0, head)
        groupPrev = dummy
        while(True):
            kth = kthNode(groupPrev, k)
            if(not kth):
                break
            groupNext = kth.next

            prev = kth.next
            current = groupPrev.next
            while(current != groupNext):
                next = current.next
                current.next = prev
                prev = current
                current = next

            next = groupPrev.next
            groupPrev.next = kth
            groupPrev = next

        return dummy.next
### Probblem 3217: Remove Linked List Elements
### tags: Array, Hash table, Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = set(nums)
        current = head
        prev = None
        while(current):
            if(current.val in hashset):
                if(current == head):
                    current = current.next
                    head = current
                else:
                    prev.next = current.next
                    current = current.next
            else:
                prev = current
                current = current.next
        return head
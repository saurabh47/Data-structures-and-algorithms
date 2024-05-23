### Problem 445. Add Two Numbers II  (Medium) https://leetcode.com/problems/add-two-numbers-ii/
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        result_head = None
        res_current = None
        carry = 0
        while(l1 and l2):
            val = l1.val + l2.val + carry
            carry = val // 10
            if(result_head is None):
                result_head = ListNode(val % 10)
                res_current = result_head
            else:
                res_current.next = ListNode(val % 10)
                res_current = res_current.next

            l1 = l1.next
            l2 = l2.next

        # l2 is None
        while(l1):
            val = l1.val + carry
            carry = val // 10
            res_current.next = ListNode(val % 10)
            res_current = res_current.next
            l1 = l1.next

        # l1 is None
        while(l2):
            val = l2.val + carry
            carry = val // 10
            res_current.next = ListNode(val % 10)
            res_current = res_current.next
            l2 = l2.next

        # both l1 and l2 were of same length
        if(carry > 0):
            res_current.next = ListNode(carry)
            res_current = res_current.next

        result_head = self.reverse(result_head)
        return result_head

    def reverse(self, root: ListNode) -> ListNode:
        current = root
        prev = None
        while(current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev


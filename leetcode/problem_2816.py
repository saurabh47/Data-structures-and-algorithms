# Problem 2816. Double the Linked List (Medium): https://leetcode.com/problems/double-the-linked-list/

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = self.reverse(head)
        carry = 0
        temp = current
        prev = None
        while(temp):
            num = temp.val*2 + carry
            temp.val = num % 10
            carry = num//10
            prev = temp
            temp = temp.next
        if(carry != 0):
            prev.next = ListNode(carry)
        return self.reverse(current)

    def reverse(self, head: ListNode)-> ListNode:
        current = head
        prev = None
        while(current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    
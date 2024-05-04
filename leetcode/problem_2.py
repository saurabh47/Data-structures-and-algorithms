# Problem 2. Add two numbers (Medium): https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        factor = 1
        head = ListNode()
        while(l1):
            num1 = num1 + l1.val * factor
            factor *= 10
            l1 = l1.next
        num2 = 0
        factor = 1
        while(l2):
            num2 = num2 + l2.val * factor
            factor *= 10
            l2 = l2.next
        result = num1 + num2
        prev = head
        if(result == 0):
            return head
        while(result != 0):
            value = result % 10
            result = result // 10
            prev.next = ListNode(value)
            prev = prev.next
        return head.next

# Optimized solution
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        current = None
        carry = 0
        while(l1 and l2):
            val = l1.val + l2.val + carry
            if(head):
                current.next = ListNode(val % 10)
                current = current.next
            else:
                head = ListNode(val % 10)
                current = head
            carry = val//10
            l1 = l1.next
            l2 = l2.next
        if(l1):
            while(l1):
                val = l1.val + carry
                carry = val // 10
                current.next = ListNode(val%10)
                current = current.next
                l1 = l1.next
        else:
            while(l2):
                val = l2.val + carry
                carry = val // 10
                current.next = ListNode(val%10)
                current = current.next
                l2 = l2.next
        if(carry):
            current.next = ListNode(carry)
            current = current.next
        return head

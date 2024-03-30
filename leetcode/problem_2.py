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

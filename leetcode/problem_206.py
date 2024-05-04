# Problem 206. Reverse Linked List (Easy): https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while(head):
            stack.append(head.val)
            head = head.next
        start = None
        if(stack):
            start = ListNode(stack.pop())
            temp = start
        while(stack):
            temp.next = ListNode(stack.pop())
            temp = temp.next
        return start

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while(current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev


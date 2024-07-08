### Problem 1823. Find the Winner of the Circular Game (Medium)
### Tags: Queue, Simulation

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        remaining = n
        head = None
        tail = None
        for i in range(1, n+1):
            if(tail is None):
                head = ListNode(i)
                tail = head
            else:
                tail.next = ListNode(i)
                tail = tail.next
        if(head.next is None):
            return head.val
        count = 0
        while(head):
            if(count == k-1):
                head = head.next
                count = 0
            else:
                # insert head at end
                tail.next = ListNode(head.val)
                tail = tail.next
                # move head 
                head = head.next
                count += 1
            if(head.next is None):
                break
        return head.val
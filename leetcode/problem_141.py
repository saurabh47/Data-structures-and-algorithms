### Problem 141. Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = {}
        start = head
        count = 0
        while(start and start not in index):
            index[start] = 0
            start = start.next
        if(start):
            return True
        return False


# Optimized
# Floyd's Tortoise and Hare Algorithm
# res: https://www.youtube.com/watch?v=RRSItF-Ts4Q

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False
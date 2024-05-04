class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        while(head not in visited and head):
            visited[head] = head
            head = head.next
        return head


# Hare and Tortoise mathematical explanation: https://www.youtube.com/watch?v=PvrxZaH_eZ4
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast  = fast.next.next
            if(slow == fast):
                slow = head
                while(slow != fast):
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
### Problem 23. Merge k Sorted Lists (Hard): https://leetcode.com/problems/merge-k-sorted-lists/
### Tags: Linked List, Heap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        result = None
        for i in range(len(lists)):
            head = lists[i]
            while(head):
                heapq.heappush(min_heap, head.val)
                head = head.next
            print(result)
        tail = None
        while(min_heap):
            popped = heapq.heappop(min_heap)
            if(result is None):
                result = ListNode(popped)
                tail = result
            else:
                tail.next = ListNode(popped)
                tail = tail.next
        return result
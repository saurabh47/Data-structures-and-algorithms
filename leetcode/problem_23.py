### Problem 23. Merge k Sorted Lists (Hard): https://leetcode.com/problems/merge-k-sorted-lists/
### Tags: Linked List, Heap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(NlogK) where N is the total number of elements in all the linked lists and K is the number of linked lists
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

# Time Complexity: O(NlogN) where N is the total number of elements in all the linked lists
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for i in range(len(lists)):
            head = lists[i]
            while(head):
                result.append(head.val)
                head = head.next
        arr = sorted(result)
        tail = None
        result = None
        i = 0
        while(i < len(arr)):
            popped = arr[i]
            if(result is None):
                result = ListNode(popped)
                tail = result
            else:
                tail.next = ListNode(popped)
                tail = tail.next
            i += 1
        return result
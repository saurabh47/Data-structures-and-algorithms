### Problem 2181. Merge Nodes by Sum (Medium)
### Tags: [Linked List]
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        result_head = None
        sum_nodes = 0
        prev = head
        start = prev.next
        while(start):
            sum_nodes += start.val
            if(start.val == 0):
                prev = start
                if(result_head is None):
                    result_head = ListNode(sum_nodes)
                    result = result_head
                else:
                    result.next = ListNode(sum_nodes)
                    result = result.next
                self.printList(result)
                sum_nodes = 0
            start = start.next
        return result_head
    
    def printList(self, head):
        result = []
        while(head):
            result.append(head.val)
            head = head.next
        return result
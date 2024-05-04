# Problem 21. Merge Two Sorted Lists (Easy): https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 and not list2):
            return list1
        if(not list1 and list2):
            return list2
        if(not list1 and not list2):
            return None
        result = ListNode(min(list1.val, list2.val))
        if(list1.val > list2.val):
            list2 = list2.next
        else:
            list1 = list1.next
        temp = result
        while(list1 and list2):
            if(list1.val > list2.val):
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
            else:
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next

        if(list1):
            while(list1):
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next
        else:
            while(list2):
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
        return result



# Problem 143. Reorder List (Medium): https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        temp = head
        while(temp):
            arr.append(temp)
            temp = temp.next
        if(len(arr) == 1):
            return head
        start = 1
        end = len(arr) -1
        temp = head
        left = True
        while(start <= end):
            if(left):
                temp.next = arr[end]
                end -= 1
            else:
                temp.next = arr[start]
                start += 1
            temp = temp.next
            left = not left
        temp.next = None  
        return head


# Time Complexity: O(n)
# Space Complexity: O(n)



        
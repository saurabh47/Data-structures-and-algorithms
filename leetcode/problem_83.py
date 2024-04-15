# Problem 83. Remove Duplicates from Sorted List (Easy): https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique = {}
        temp = head
        prev = temp
        while(temp):
            if(temp.val in unique):
                prev.next = temp.next
            else:
                unique[temp.val] = temp
                prev = temp
            temp = temp.next;
        return head

# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == '__main__':
    s = Solution()
    print(s.deleteDuplicates([1,1,2])) # [1,2]
    print(s.deleteDuplicates([1,1,2,3,3])) # [1,2,3]
    print(s.deleteDuplicates([1,1,1,1,1])) # [1]
    print(s.deleteDuplicates([1,2,3,4,5])) # [1,2,3,4,5]
    print(s.deleteDuplicates([1,2,2,3,3,4,4,5,5])) # [1,2,3,4,5]
    print(s.deleteDuplicates([1,1,1,2,2,3,3,4,4,5,5])) # [1,2,3,4,5]

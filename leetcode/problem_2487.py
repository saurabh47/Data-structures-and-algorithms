# Problem 2487. Remove Smallest Node in Linked List (Medium): https://leetcode.com/problems/remove-smallest-node-in-linked-list/

# hint: reverse the linked list and then iterate through the linked list to remove the smallest node
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = self.reverse(head)
        res_head = current
        smallest = current.val
        while(current):
            if(current.val < smallest):
                prev.next = current.next
                current = current.next
            else:
                smallest = current.val
                prev = current
                current = current.next
        prev = None
        result  = self.reverse(res_head)
        return result

    # Reverse the linked list
    def reverse(self, head: ListNode)-> ListNode:
        prev = None
        current = head
        while(current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
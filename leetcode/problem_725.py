### Problem 725. Split Linked List in Parts (Medium): https://leetcode.com/problems/split-linked-list-in-parts/

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        result = []
        while(current):
            current = current.next
            length += 1
        splitSize = 1
        remainder = 0
        splitSize = length//k
        remainder = length % k
        current = head
        part = 0
        while(k > part):
            count = 0
            size_k = 1 if remainder else 0
            result.append(current)
            while(current and count < (splitSize - 1 + size_k)):
                current = current.next
                count += 1
            remainder -= size_k
            if(current):
                temp = current.next
                current.next = None
                current = temp
            part += 1
        return result
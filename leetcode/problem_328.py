### Problem 328. Odd Even Linked List (Medium) https://leetcode.com/problems/odd-even-linked-list/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = None
        even_ptr = None
        temp = head
        prev = temp
        index = 1
        if(not head or not head.next):
            return head
        while(temp):
            if(index % 2 == 0):
                if(not even_head):
                    even_head = ListNode(temp.val)
                    even_ptr = even_head
                else:
                    even_ptr.next = ListNode(temp.val)
                    even_ptr = even_ptr.next
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
            index += 1
        prev.next = even_head
        return head

# Time complexity: O(n)
# Space complexity: O(1)

if __name__ == '__main__':
    s = Solution()
    print(s.oddEvenList([1,2,3,4,5,6,7,8])) # [1,3,5,7,2,4,6,8]
    print(s.oddEvenList([1,2,3,4,5,6,7,8,9,10])) # [1,3,5,7,9,2,4,6,8,10]
    print(s.oddEvenList([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # [1,3,5,7,9,11,13,15,17,19,2,4,6,8,10,12,14,16,18,20]
    print(s.oddEvenList([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])) # [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    print(s.oddEvenList([1,2,3,4,5])) # [1,3,5,2,4]
    print(s.oddEvenList([1,2,3,4,5,6])) # [1,3,5,2,4,6]
    print(s.oddEvenList([1])) # [1]
    print(s.oddEvenList([1,2])) # [1,2]
    print(s.oddEvenList([1,2,3])) # [1,3,2]
    print(s.oddEvenList([1,2,3,4])) # [1,3,2,4]

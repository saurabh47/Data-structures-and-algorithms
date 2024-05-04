# Problem 876. Middle of the Linked List (Easy): https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while(temp):
            length += 1
            temp = temp.next
        length = int(length // 2)
        current = -1
        print(length)
        while(current < length-1):
            head = head.next
            current +=1
        return head

# Optimized solution usinng tortoise and hare
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow    

# Time complexity: O(n)
# Space complexity: O(1)

if __name__ == '__main__':
    s = Solution()
    print(s.middleNode([1,2,3,4,5])) # [3,4,5]
    print(s.middleNode([1,2,3,4,5,6])) # [4,5,6]
    print(s.middleNode([1])) # [1]
    print(s.middleNode([1,2])) # [2]
    print(s.middleNode([1,2,3])) # [2,3]
    print(s.middleNode([1,2,3,4])) # [3,4]
    print(s.middleNode([1,2,3,4,5,6,7,8,9,10])) # [6,7,8,9,10]
    print(s.middleNode([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # [11,12,13,14,15,16,17,18,19,20]
    print(s.middleNode([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])) # [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
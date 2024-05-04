# Problem 234. Palindrome Linked List (Easy): https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        start = head
        forward =  ''
        while(start):
            forward += str(start.val)
            start = start.next
        return forward == forward[::-1]


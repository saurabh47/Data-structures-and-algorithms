class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        addr = {}
        if(not headA or not headB):
            return None
        while(headA):
            addr[headA] = headA
            headA = headA.next
        while(headB):
            if(headB in addr):
                return headB
            headB = headB.next
        return None
    
# Time complexity: O(n)
# Space complexity: O(n)


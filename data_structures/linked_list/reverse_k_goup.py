import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from data_structures.linked_list.node import Node
from traversal import LinkedList

class Solution:
    def reverseKGroup(self, head, k: int):
        def kthNode(current, k):
            while(current and k > 0):
                current = current.next
                k-= 1
            return current

        dummy = Node(0, head)
        groupPrev = dummy
        while(True):
            kth = kthNode(groupPrev, k)
            if(not kth):
                break
            groupNext = kth.next

            prev = kth.next
            current = groupPrev.next
            while(current != groupNext):
                next = current.next
                current.next = prev
                prev = current
                current = next

            next = groupPrev.next
            groupPrev.next = kth
            groupPrev = next
        return dummy.next

    def printList(self, head):
        result = []
        while(head):
            result.append(head.data)
            head = head.next
        return result


if __name__ == '__main__':
    s = Solution()
    input_list = [1,2,3,4,5,6,7,8]
    linkedList =  LinkedList(input_list)
    res = s.reverseKGroup(linkedList.head, 3)
    linkedList.iterateList(res)
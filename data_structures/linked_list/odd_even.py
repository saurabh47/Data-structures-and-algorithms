import sys
sys.path.append('../linked_list')
from traversal import LinkedList
from node import Node

class Solution:
    def oddEvenList(self, head: Node):
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
                    even_head = Node(temp.data)
                    even_ptr = even_head
                else:
                    even_ptr.next = Node(temp.data)
                    even_ptr = even_ptr.next
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next

            index += 1
        prev.next = even_head
        return head

if __name__ == '__main__':
    s = Solution()
    input_list = [1,2,3,4,5,6,7,8]
    linkedList =  LinkedList(input_list)
    res = s.oddEvenList(linkedList.head)
    linkedList.iterateList(res)
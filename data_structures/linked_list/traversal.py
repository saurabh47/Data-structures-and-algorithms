import sys
sys.path.append('../linked_list')
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def arrayToList(self, arr):
        start = Node(arr[0])
        temp = start
        for i in range(1, len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next
        return start

    def iterateList(self, head):
        while(head):
            print(head.data)
            head = head.next


if __name__ =='__main__':
    list =  LinkedList()
    head = list.arrayToList([1, 2, 4, 5, 2, 3, 12, 34, 56])
    list.iterateList(head)

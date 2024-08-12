
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from data_structures.linked_list.node import Node

class LinkedList:
    def __init__(self, arr = []):
        if(len(arr) > 0):
            self.head = self.arrayToList(arr)
        else:
            self.head = None

    def arrayToList(self, arr):
        start = Node(arr[0])
        temp = start
        for i in range(1, len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next
        return start

    def iterateList(self, head=None):
        head = self.head if head == None else head
        while(head):
            print(head.data)
            head = head.next

    def reorderList(self, head):
        print("Reordering")
        arr = []
        temp = head
        while(temp):
            arr.append(temp)
            temp = temp.next
        if(len(arr) == 1):
            return head
        start = 1
        end = len(arr) -1
        temp = head
        left = True
        while(start <= end):
            if(left):
                temp.next = arr[end]
                end -= 1
            else:
                temp.next = arr[start]
                start += 1
            print(start, ",",end)
            temp = temp.next
            left = not left
        temp.next = None  
        return head



if __name__ =='__main__':
    list =  LinkedList()
    head = list.arrayToList([1, 2, 4, 5, 12, 3, 32, 34, 56])
    # head = list.reorderList(head)
    list.iterateList(head)

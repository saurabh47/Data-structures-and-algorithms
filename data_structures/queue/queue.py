import sys
sys.path.append('../../data_structures')
from data_structures.linked_list.node import Node

class Queue:
    def __init__(self, head = None, tail = None):
        self.head = None
        self.tail = None

    def push(self, val:int):
        if(self.head):
            self.tail.next = Node(val)
            self.tail = self.tail.next
        else:
            self.head = Node(val)
            self.tail = self.head

    def popFront(self):
        if(not self.head):
            return
        temp = self.head
        self.head = self.head.next
        return temp.data

    def printQueue(self):
        result = []
        current = self.head
        while(current):
            result.append(current.data)
            current = current.next
        return result

if __name__ == '__main__':
    q =  Queue()
    temp = [2, 3, 5, 1, 12, 44, 10, 4, 7, 9, 8]
    q.popFront()
    for num in temp:
        q.push(num)
    q.popFront()
    q.popFront()
    print("queue:",q.printQueue())
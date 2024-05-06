### Problem 622. Design Circular Queue (Medium): https://leetcode.com/problems/design-circular-queue/
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.head = None
        self.tail = None    

    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        if(self.head is None):
            self.head = Node(value)
            self.tail = self.head
            self.tail.next = self.head
        else:
           self.tail.next = Node(value)
           self.tail = self.tail.next
           self.tail.next = self.head
        self.size += 1
        return True 

    def deQueue(self) -> bool:
        if(self.head is None):
            return False
        if(self.head == self.tail):
            self.size -= 1
            self.head = None
            self.tail = None
            return True
        self.tail.next = self.head.next
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if(self.head is None):
            return -1
        else:
            return self.head.val

    def Rear(self) -> int:
        if(self.tail is None):
            return -1
        else:
            return self.tail.val

    def isEmpty(self) -> bool:
        return self.head is None and self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
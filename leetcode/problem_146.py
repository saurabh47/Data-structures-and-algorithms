# Problem 146. LRU Cache (Medium): https://leetcode.com/problems/lru-cache/

# Note: Do not attempt this question
# if you are not familiar with the concept of linked list.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.lastPointer = None
        self.size = 0
        self.cache = {}

    def removeNode(self, val:int) -> Node: 
        prev = None
        current = self.head
        while current:
            if current.val == val:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current == self.lastPointer:
                    self.lastPointer = prev
                return current
            prev = current
            current = current.next

    def removeFront(self)-> Node: 
        print("remove Front:", self.cache)
        current = self.head
        if(self.head):
            self.head = self.head.next
        print("after removeFront:", self.cache)
        return current

    def insertLast(self, val:int):
        if self.head:
            self.lastPointer.next = Node(val)
            self.lastPointer = self.lastPointer.next
        else:
            self.head = Node(val)
            self.lastPointer = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.removeNode(key)
            self.insertLast(node.val)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.size >= self.capacity:
                del self.cache[self.head.val]
                self.removeNode(self.head.val)
            else:
                self.size += 1
            self.insertLast(key)
        else:
            self.removeNode(key)
            self.insertLast(key)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
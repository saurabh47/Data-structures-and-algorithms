# Problem 146. LRU Cache (Medium): https://leetcode.com/problems/lru-cache/

# Note: Do not attempt this question
# if you are not familiar with the concept of linked list.

class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # head = MRU, tail = LRU
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.cache = {}
        self.size = 0

    def get(self, key: int) -> int:
        if(key in self.cache):
            pointer = self.cache[key]
            self.removeNode(pointer)
            self.insertNode(pointer)
            return pointer.val
        else:
            return -1

    # insert Front
    def insertNode(self, node):
        if(self.head is None):
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node

    def deleteEnd(self):
        if(not self.tail):
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def removeNode(self, curr):
        if(curr is None):
            return
        # only 1 element
        if(not curr.prev and not curr.next):
            self.head = None
            self.tail = None
        # last element
        elif(curr.prev and not curr.next):
            curr.prev.next = None
            self.tail = curr.prev
        # first element
        elif(not curr.prev and curr.next):
            self.head = curr.next
            self.head.prev = None
        # delete in between
        else:
            prev = curr.prev
            next = curr.next
            prev.next = next
            next.prev = prev

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            self.removeNode(self.cache[key])
            self.size -= 1  #
        node = Node(key, value)
        self.insertNode(node)
        self.cache[key] = node
        self.size += 1
        while(self.size > self.capacity):
            del self.cache[self.tail.key]
            self.deleteEnd()
            self.size -=1

    def showCache(self):
        result= []
        for key, pointer in self.cache.items():
            result.append((key, pointer.val))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
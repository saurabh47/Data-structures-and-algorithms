class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def hasNext(self):
        return self.next != None

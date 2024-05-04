class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def hasNext(self):
        return self.next != None

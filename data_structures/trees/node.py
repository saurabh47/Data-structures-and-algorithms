# Define a class Node with data, left, and right attributes.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def hasChild(self):
        return self.left != None or self.right != None
    def hasLeftChild(self):
        return self.left != None

    def hasRightChild(self):
        return self.right != None


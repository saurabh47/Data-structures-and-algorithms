### Problem 1381. Design a Stack With Increment Operation (Medium): https://leetcode.com/problems/design-a-stack-with-increment-operation/

### tags: array, stack, design
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if(self.isFull()): return
        self.stack.append(x)

    def pop(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val

    def isFull(self):
        return len(self.stack) == self.maxSize

    def isEmpty(self):
        return len(self.stack) == 0

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
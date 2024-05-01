### Problem 232. Implement Queue using Stacks (Easy): https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack =[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if(self.stack):
            return self.stack.pop(0)

    def peek(self) -> int:
        if(self.stack):
            return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
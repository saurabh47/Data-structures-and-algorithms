### Problem 933. Number of Recent Calls (Easy): https://leetcode.com/problems/number-of-recent-calls/

### Tags: Queue
from queue import Queue
class RecentCounter:
    def __init__(self):
        self.q = Queue()

    def ping(self, t: int) -> int:
        self.q.put(t)
        top = self.q.queue[0]
        if(top < t - 3000):
            while(top < t - 3000):
                self.q.get()
                top = self.q.queue[0]
        return self.q.qsize()
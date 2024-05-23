### Problem 295. Find Median from Data Stream (Hard): https://leetcode.com/problems/find-median-from-data-stream/
# Tags: Heap, Design
class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        self.heap.append(num)

    def findMedian(self) -> float:
        self.heap = sorted(self.heap)
        size = len(self.heap)
        if(size % 2==0):
            return (self.heap[size//2] + self.heap[(size // 2) -1]) / 2
        else:
            return self.heap[size//2]


### Optimized

class MedianFinder:

    def __init__(self):
        self.lheap = []
        self.rheap = []

    def addNum(self, num: int) -> None:
        if(len(self.lheap) == 0):
            self.lheap.append(num*-1)
            return
        if(len(self.lheap) > len(self.rheap)):
            if(num > self.lheap[0]*-1):
                heapq.heappush(self.rheap, num)
            else:
                heapq.heappush(self.rheap, self.lheap[0]*-1)
                heapq.heappop(self.lheap)
                heapq.heappush(self.lheap, num * -1)
        else:
            if(num > self.lheap[0]*-1):
                heapq.heappush(self.rheap, num)
                heapq.heappush(self.lheap, self.rheap[0]*-1)
                heapq.heappop(self.rheap)
            else:
                heapq.heappush(self.lheap, num*-1)
        
    def findMedian(self) -> float:
        if(len(self.lheap) == len(self.rheap)):
            return ((self.lheap[0]*-1) + self.rheap[0])/2
        else:
            return self.lheap[0]*-1



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
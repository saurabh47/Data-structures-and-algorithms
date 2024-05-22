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



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
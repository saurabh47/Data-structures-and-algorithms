class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.harr = nums
        self.k = k
        # creates min heap
        heapq.heapify(self.harr)
        while(len(self.harr) > k):
           heapq.heappop(self.harr)

    def add(self, val: int) -> int:
        heapq.heappush(self.harr, val)
        if(self.k < len(self.harr)):
            heapq.heappop(self.harr)
        return self.harr[0]

class MinHeap:
    def __init__(self, capacity):
        # defines the maximum number of elements that can be stored in the heap
        self.capacity = capacity
        # defines the current number of elements in the heap
        self.size = 0
        # defines the array to store the elements
        self.arr = []

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    # time complexity log(n) or height of tree
    def insert(self, val):
        if(self.size >= self.capacity):
            print("heap is full")
            return
        self.size += 1
        self.arr.append(val)
        if(self.size > 1):
            i = self.size - 1
            p = self.parent(i)
            node = self.arr[i]
            while(i !=0 and self.arr[p] > node):
                self.swap(p, i)
                i = p
                p = self.parent(i)
                node = self.arr[i]
        print(val, "inserted in heap")

    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j]= temp

if __name__ == '__main__':
    minHeap = MinHeap(20)
    minHeap.insert(20)
    minHeap.insert(50)
    minHeap.insert(10)
    minHeap.insert(40)
    minHeap.insert(15)
    minHeap.insert(100)
    minHeap.insert(45)
    minHeap.insert(25)
    # for i in range(20, 0, -1):
    #     minHeap.insert(i)
    print(minHeap.arr, minHeap.size, minHeap.capacity)
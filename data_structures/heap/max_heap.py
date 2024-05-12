class MaxHeap:
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

    def get_max(self):
        if(self.arr):
            return self.arr[0]
        print("heap is empty")

    # removes and returns root of heap arr[0]
    def extract_max(self):
        if(self.size == 0):
            print("heap is empty")
            return
        maximum = self.arr[0]
        if(self.size == 1):
            self.size -= 1
            return self.arr.pop()
        if(self.size > 1):
            self.size -= 1
            self.swap(0, self.size)
            self.arr.pop()
            self.max_heapify(0)
        return maximum

    # max heapify at node index i
    # This is called to fix node i in a heap
    def max_heapify(self, i:int):
        largest = i
        left = self.left(i)
        right = self.right(i)
        if(left < self.size and self.arr[left] > self.arr[largest]):
            largest = left
        if(right < self.size and self.arr[right] > self.arr[largest]):
            largest = right
        if(largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)

    # Creates a max heap from an array
    def build_max_heap(self, arr):
        # find the bottom right parent
        self.arr = arr
        self.size = len(arr)
        ri  = self.parent(len(self.arr)- 1)
        for i in range(ri, -1, -1):
            self.max_heapify(i)

    # time complexity log(n) or height of tree
    # To insert in a min_heap
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
            while(i !=0 and self.arr[p] < node):
                self.swap(p, i)
                i = p
                p = self.parent(i)
                node = self.arr[i]
        print(val, "inserted in heap")

    def heapSort(self):
        for i in range(len(self.arr)- 1, 0, -1):
            self.swap(0, i)
            self.size -=1
            self.max_heapify(0)

    def delete(self, index):
        print("deleting", self.arr[index])
        if(self.size <= 0):
            print("heap is empty")
            return
        if(index >= self.size):
            print("index out of bounds")
            return
        self.size -= 1
        self.swap(index, self.size)
        deleted = self.arr.pop()
        self.max_heapify(index)
        print(deleted, " deleted from the heap",)
        return deleted

    def decrease(self, val, k):
        index = k
        if(self.size <= 0):
            print("heap is empty")
            return
        if(index >= self.size):
            print("index out of bounds")
            return
        if(self.arr[index] <= val):
            print("value to be decreased at {} should be less than {}".format(index,self.arr[index]))
            return
        self.arr[index] = val
        p = self.parent(index)
        while(index != 0 and self.arr[p] > self.arr[index]):
                self.swap(p,index)
                index = p
                p = self.parent(index)
        print("decreased the element", val, "at ", k)

    def swap(self, i, j):
        if(i == j):
            return
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j]= temp

    #  Min Heap                                         20
    #                40                               /     \
    #              /    \                            /       \
    #            20      30       Min Heap          25        30
    #          /   \    /  \      ------->        /   \      /   \
    #        35     25 80   32                   40    35   80   32
    #       /  \   /                           /  \   /
    #      100 70 60                         100  70 60
    #



if __name__ == '__main__':
    heap = MaxHeap(20)
    arr = [40, 20, 30, 35, 25, 80, 32, 100, 70, 60]
    for num in arr:
        heap.insert(num)
    print("max heap:", heap.arr)
    print("maximum:", heap.get_max(),heap.size)
    print("extract:", heap.extract_max(),heap.size)
    print("max heap:", heap.arr,heap.size)
    heap.delete(4)
    print("max heap:", heap.arr,heap.size)
    print("decreased:", heap.decrease(20, 1),heap.size)
    heap.build_max_heap(arr)
    print("max heap:", heap.arr, heap.size)
    print(heap.arr,"size:", heap.size,"capacity:", heap.capacity)
    heap.heapSort()
    print("sorted heap:", heap.arr, heap.size)
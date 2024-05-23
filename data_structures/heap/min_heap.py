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

    def get_min(self):
        if(self.arr):
            return self.arr[0]
        print("heap is empty")

    # removes and returns root of heap arr[0]
    def extract_min(self):
        if(self.size == 0):
            print("heap is empty")
            return
        minimum = self.arr[0]
        if(self.size == 1):
            self.size -= 1
            return self.arr.pop()
        if(self.size > 1):
            self.size -= 1
            self.swap(0, self.size)
            self.arr.pop()
            self.min_heapify(0)
        return minimum

    # Given an array create min Heap
    def build_min_heap(self, arr):
        self.arr = arr
        self.size = len(arr)
        # get the bottom most parent with
        ri  = self.parent(len(self.arr) -1)
        for i in range(ri, -1, -1):
            self.min_heapify(i)
        print("heap built:")

    # converts the binary tree to min heap
    # input is index i at which heapfiy has to be checked
    def min_heapify(self, i:int):
        smallest = i
        right = self.right(i)
        left = self.left(i)
        if(left < self.size and self.arr[left] < self.arr[smallest]):
           smallest = left
        if(right < self.size and self.arr[right] < self.arr[smallest]):
           smallest = right
        if(smallest != i):
            self.swap(smallest, i)
            self.min_heapify(smallest)

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
            while(i !=0 and self.arr[p] > node):
                self.swap(p, i)
                i = p
                p = self.parent(i)
                node = self.arr[i]
        print(val, "inserted in heap")

    def delete(self, index):
        if(self.size <= 0):
            print("heap is empty")
            return
        if(index >= self.size):
            print("index out of bounds")
            return
        self.size -= 1
        self.swap(index, self.size)
        deleted = self.arr.pop()
        self.min_heapify(index)
        print(deleted, " deleted from the heap")
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
    heap = MinHeap(20)
    arr = [40, 20, 30, 35, 25, 80, 32, 100, 70, 60]
    for num in arr:
        heap.insert(num)
    print("min heap:", heap.arr)
    print("minimum:", heap.get_min())
    print("extract:", heap.extract_min())
    print("min heap:", heap.arr)
    print("delete:", heap.delete(4))
    print("min heap:", heap.arr)
    print("decreased:", heap.decrease(20, 1))
    print("min heap:", heap.arr)
    arr = [72,12,40, 20, 30, 35, 25, 100, 70, 60]
    print("build min heap: ", heap.build_min_heap(arr))
    print("min heap:", heap.arr)
    # print(heap.arr, heap.size, heap.capacity)
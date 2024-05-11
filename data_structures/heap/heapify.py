# heapfiy is a concept used in heaps. This is a process to mitigate the violation of the heap property.
import sys
sys.path.append('../heap')
from min_heap import MinHeap


class Heapify(MinHeap):

    # converts the binary tree to min heap
    # input is a heap and index i at which heapfiy has to be checked
    def min_heapify(self, heap: MinHeap, i:int):
        root = i
        smallest = i
        right = heap.right(i)
        left = heap.left(i)
        if(left < heap.size and heap.arr[left] < heap.arr[smallest]):
           smallest = left
        if(right < heap.size and heap.arr[right] < heap.arr[smallest]):
           smallest = right
        if(smallest != i):
            heap.swap(smallest, i)
            self.min_heapify(heap, smallest)

    # converts the binary tree to max heap
    def max_heapify(self, heap):
        pass

if __name__ == '__main__':
    heap = MinHeap(20)
    heap.insert(32)
    heap.insert(25)
    heap.insert(80)
    heap.insert(60)
    heap.insert(40)
    heap.insert(100)
    heap.insert(35)
    heap.insert(30)
    heap.insert(20)
    heap.insert(70)
    print(heap.arr)
    h = Heapify(20)
    heap.arr = [40, 20, 30, 35, 25,80, 32, 100, 70, 60]
    h.min_heapify(heap, 8)
    print(heap.arr)
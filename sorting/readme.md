# Sorting Algorithms

1. Selection Sort
   Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    > Selection Sort cannot be optimized to perform better than O(n^2) in terms of time complexity. Even if you maintain a min index array, the time complexity remains the same. Because the original changes after swap which will invalidate the min index array.
    
    The problems with selection sort are:
    - It has O(n^2) time complexity, which makes it inefficient on large lists.
    - The time complexity is still O(N^2) even if the list is already sorted.
    - It has O(n) swaps, which is not ideal for memory usage.


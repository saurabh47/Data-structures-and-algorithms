# Selection Sort

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i, len(arr)):
            if(arr[j] < arr[smallest]):
                smallest = j
        swap(smallest, i)
        print(arr)
    print("sorted arr=", arr)

print("Enter the number of elements in the array")
n = int(input())
print("Enter the elements of the array")
arr = list(map(int, input().split()))
selection_sort(arr)
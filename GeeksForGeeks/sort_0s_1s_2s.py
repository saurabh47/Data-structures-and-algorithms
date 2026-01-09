class Solution:
    def sort012(self, arr):
        
        def swap(i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        
        fixedVal = 0
        for i in range(len(arr)):
            num = arr[i]
            if(num == fixedVal):
                continue
            j = i + 1
            while(j < len(arr)):
                if(arr[j] == fixedVal):
                    swap(i, j)
                    break
                if(arr[i] > arr[j]):
                    swap(i, j)
                j += 1

            if(j == len(arr)):
                fixedVal += 1

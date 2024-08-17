### Problem 1122. Relative Sort Array (Easy): https://leetcode.com/problems/relative-sort-array/
### Tags: Array, Hash Table, Sorting

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        freq2 = {}
        result = []
        for i in range(len(arr1)):
            if(arr1[i] in freq):
                freq[arr1[i]] += 1
            else:
                freq[arr1[i]] = 1

            if(i < len(arr2)):
                freq2[arr2[i]] = 1

        for i in range(len(arr2)):
            while(freq[arr2[i]] > 0):
                result.append(arr2[i])
                freq[arr2[i]] -= 1
        end = []
        for i in range(len(arr1)):
            if(arr1[i] not in freq2):
                end.append(arr1[i])

        end.sort()
        for i in range(len(end)):
            result.append(end[i])
        return result

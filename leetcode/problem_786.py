### Problem 786. K-th Smallest Prime Fraction (Medium)
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pairs = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                pairs.append((arr[i], arr[j]))

        sorted_pairs = self.mergeSort(0, len(pairs) - 1,pairs)
        return [sorted_pairs[k-1][0],sorted_pairs[k-1][1]]

    # [(1, 2), (1, 3), (1, 5), (2, 3), (2, 5), (3, 5)]
    # [2, 4, 1, 5], [3, 9, 8]
    # [2, 4], [1, 5], [3] [9, 8]

    def mergeSort(self, start:int, end:int, pairs):
        if(start == end):
            return [pairs[start]]
        mid = start + (end - start) // 2
        left = self.mergeSort(start, mid, pairs)
        right = self.mergeSort(mid+1, end, pairs)
        return self.mergeHalves(left,right)

    def mergeHalves(self, left:[], right: []):
        i = 0
        j = 0
        result = []
        while(i < len(left) and j < len(right)):
            a, b = left[i]
            c, d = right[j]
            if((a/b) > (c / d)):
                result.append(right[j])
                j+=1
            else:
                result.append(left[i])
                i+=1

        while(i < len(left)):
            result.append(left[i])
            i+=1
        while(j < len(right)):
            result.append(right[j])
            j+=1
        return result


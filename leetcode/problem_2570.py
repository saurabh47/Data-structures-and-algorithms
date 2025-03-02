#### Problem 2570. Merge Two 2D Arrays by Summing Values
#### tags: [array]
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = [] 
        nm1 = {}
        nm2 = {}
        max_k = 0
        for k, v in nums1:
            nm1[k] = v
            max_k = max(max_k, k)
        for k, v in nums2:
            nm2[k] = v
            max_k = max(max_k, k)

        for i in range(1, max_k + 1):
            if(i in nm1 and i in nm2):
                result.append([i, nm1[i] + nm2[i]])
            else:
                if(i in nm1):
                    result.append([i, nm1[i]])
                if(i in nm2):
                    result.append([i, nm2[i]])
        return result
        
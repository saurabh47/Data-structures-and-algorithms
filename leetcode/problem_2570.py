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
        
        
### Optimized Solution

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = [] 
        i,j = 0, 0
        while(i < len(nums1) and j < len(nums2)):
            k1, v1 = nums1[i]
            k2, v2 = nums2[j]
            if(k1 < k2):
                result.append([k1, v1])
                i += 1
            elif(k2 < k1):
                result.append([k2, v2])
                j += 1
            else:
                result.append([k2, v1 + v2])
                i += 1
                j += 1
        while(i < len(nums1)):
            k, v = nums1[i]
            result.append([k, v])
            i += 1
        while(j < len(nums2)):
            k, v = nums2[j]
            result.append([k, v])
            j += 1
        return result
        
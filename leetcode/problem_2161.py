### Problem 2161. Partition Array According to Given Pivot
### tags: [array, two-pointers]

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:       
        lt, gt, pv = [], [], []
        for num in nums:
            if(num < pivot):
                lt.append(num)
            elif(num > pivot):
                gt.append(num)
            else:
                pv.append(num)
        lt.extend(pv)
        lt.extend(gt)
        return lt

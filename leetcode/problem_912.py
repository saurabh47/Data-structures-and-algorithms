class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums)-1)

    def mergeSort(self, nums, start,  end):
        if(start == end):
            return [nums[start]]
        mid = start + (end - start) //2
        left = self.mergeSort(nums, start, mid)
        right = self.mergeSort(nums, mid + 1, end)
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int])-> List[int]:
        result = []
        l = len(left)
        r = len(right)
        lptr, rptr = 0, 0
        while(lptr < l and rptr < r):
            if(left[lptr] <= right[rptr]):
                result.append(left[lptr])
                lptr += 1
            else:
                result.append(right[rptr])
                rptr += 1
        if(lptr == l):
            while(rptr != r):
                result.append(right[rptr])
                rptr += 1
        else:
            while(lptr != l):
                result.append(left[lptr])
                lptr += 1
        return result
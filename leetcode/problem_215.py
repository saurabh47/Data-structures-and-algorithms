# Problem 215: Kth Largest Element in an Array (Medium): https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_array = self.merge_sort(nums)
        return sorted_array[len(sorted_array) - k]

    def mergeHalves(self,left,right):
        len_left = len(left)
        len_right = len(right)
        merged = []
        ldx = 0
        rdx = 0
        for i in range(0, (len_left+len_right)):
            if(ldx>=len_left):
                merged.append(right[rdx])
                rdx+=1
            elif(rdx >= len_right):
                merged.append(left[ldx])
                ldx+=1;
            else:
                if(left[ldx]< right[rdx]):
                    merged.append(left[ldx])
                    ldx+=1
                else:
                    merged.append(right[rdx])
                    rdx+=1
        return merged

    def merge_sort(self, array):
        start = 0
        end = len(array) - 1
        if(len(array) <= 1):
            return array
        else:
            mid = (end - start) // 2
            left_array = array[start : mid + 1]
            right_array = array[mid+1 : end + 1]
            left_half = self.merge_sort(left_array) # left_half
            right_half = self.merge_sort(right_array) # right_half
            return self.mergeHalves(left_half,right_half)
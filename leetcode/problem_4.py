# Problem 4: Median of Two Sorted Arrays (Hard): https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        sorted_arr = []
        if(len1 == 0 and len2!=0):
            return self.median(nums2, len2)
        elif(len2 == 0 and len1 != 0):
            return self.median(nums1,len1)
        left = 0
        right = 0
        isLen1Max = len1 > len2
        while(left != len1 and right != len2):
            if(nums1[left] > nums2[right]):
                sorted_arr.append(nums2[right])
                right += 1
            else:
                sorted_arr.append(nums1[left])
                left += 1
        if(left != len1):
            for i in range(left, len1):
                sorted_arr.append(nums1[i])
        else:
            for i in range(right, len2):
                sorted_arr.append(nums2[i])
        return self.median(sorted_arr, len(sorted_arr))

    def median(self, nums, size):
        if(size % 2 == 0):
           return (nums[(size//2)-1] + nums[size//2]) / 2
        else:
            return nums[size//2]

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,3],[2])) # 2.0
    print(s.findMedianSortedArrays([1,2],[3,4])) # 2.5
    print(s.findMedianSortedArrays([0,0],[0,0])) # 0.0
    print(s.findMedianSortedArrays([],[1])) # 1.0
    print(s.findMedianSortedArrays([2],[])) # 2.0
    print(s.findMedianSortedArrays([1,3],[2,7])) # 2.5
    print(s.findMedianSortedArrays([1,3,5,7,9],[2,4,6,8,10])) # 5.5
    print(s.findMedianSortedArrays([1,3,5,7,9],[2,4,6,8])) # 5.0
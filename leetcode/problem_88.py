# Problem 88: Merge Sorted Array (Easy): https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1, m, nums2, n):
        if(m == 0 and n != 0):
            right = n-1
            i = right
            while(right != -1):
                nums1[i] = nums2[right]
                right -= 1 
                i -= 1
        elif(m != 0 and n != 0):
            left = m-1
            right = n-1
            current  = m+n-1
            while(left != -1 and right != -1):
                if(nums1[left] > nums2[right]):
                    nums1[current] = nums1[left]
                    left -= 1
                else:
                    nums1[current] = nums2[right]
                    right -=1
                current -=1
            # [4, 5, 6, 0, 0, 0]
            # [1, 2, 3]
            print(nums1, left, right)
            if(left == -1):
                while(right != -1):
                    nums1[current] = nums2[right]
                    right -= 1
                    current -=1

if __name__ == "__main__":
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1) # [1,2,3,4,5,6]
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1) # [1,2,2,3,5,6]
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1) # [1]
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1) # [1,2]
    nums1 = [1,2,4,5,6,0]
    m = 5
    nums2 = [3]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1) # [1,2,3,4,5,6]
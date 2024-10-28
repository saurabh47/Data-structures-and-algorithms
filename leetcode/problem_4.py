# Problem 4: Median of Two Sorted Arrays (Hard): https://leetcode.com/problems/median-of-two-sorted-arrays/

# Naive solution 
# Time: O(n+m) where n is the length of nums1 and m is the length of nums2
# Space: O(n+m) where n is the length of nums1 and m is the length of nums2
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i = 0
        j = 0
        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i] < nums2[j]):
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while(i < len(nums1)):
            result.append(nums1[i])
            i += 1
        while(j < len(nums2)):
            result.append(nums2[j])
            j += 1
        length = len(result)
        if length & 1:  
            return result[length // 2] 
        else: 
            return (result[length // 2] + result[(length // 2) -1]) / 2

# O(n+m) solution

class Solution2:
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

# O(1) space complexity
# O(m+n) time complexity
# hint:We traverse to middle by choosing the smallest from both arrays and keep track of recent two elements.
class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)
        odd = m+n & 1
        prev = 0
        curr = 0
        i = 0
        j = 0
        index = 0
        while(i < m and j < n):
            if(index == ((m + n)// 2) + 1):
                break
            prev = curr
            if(nums1[i] < nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            index += 1

        if(index == ((m + n)// 2) + 1):
            if(odd):
                return curr
            return (curr + prev) / 2
        else:
            if(i < m):
                while(index != ((m + n)// 2) + 1):
                    prev = curr 
                    curr = nums1[i]
                    index += 1
                    i += 1
            else:
                while(index != ((m + n)// 2) + 1):
                    prev = curr 
                    curr = nums2[j]
                    index += 1
                    j += 1
        if(odd):
            return curr
        return (curr + prev) / 2
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
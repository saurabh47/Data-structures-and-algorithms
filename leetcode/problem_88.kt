# Problem 88: Merge Sorted Array (Easy): https://leetcode.com/problems/merge-sorted-array/

class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        var left = m - 1
        var right = n - 1
        var i = nums1.size - 1
        while(left >= 0 && right >= 0){
            if(nums1[left] > nums2[right]){
                nums1[i] = nums1[left]
                left -= 1
            }else{
                nums1[i] = nums2[right]
                right -= 1
            }
            i -= 1
        }
        // right is zero
        while(left >= 0){
            nums1[i] = nums1[left]
            left -= 1
            i -= 1
        }
        // left is zero
        while(right >= 0){
            nums1[i] = nums2[right]
            right -= 1
            i -= 1
        }
    }
}
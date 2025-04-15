// Problem 33. Search in Rotated Sorted Array
// Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
// tags: Binary Search, Array

// The idea is to find a pivot and apply binary search in one of the partition
class Solution {
    fun search(nums: IntArray, target: Int): Int {
        /* given: arr, target
         * output:index of target
         * 
         */

        var start = 0
        var end = nums.size - 1
        var pivot = -1
        while(start < end){
            var mid = start + (end - start) / 2
            if(nums[mid] == target){
                return mid
            }
            if(mid < nums.size - 1 && nums[mid] > nums[mid + 1]){
                pivot = mid + 1
                break
            }
            if(mid > 0 && nums[mid] < nums[mid - 1]){
                pivot = mid
                break
            }
            if(nums[start] < nums[mid]){
                start = mid + 1
            }else{
                end = mid - 1
            }
        }
        if(pivot == -1){
            pivot = start  
        }
        // println("pivot=$pivot")
        if(nums[pivot] == target){
            return pivot
        }
        // // 0 - pivot  end
        if(pivot > 0 && nums[0] <= target && target <= nums[pivot - 1]){
            start = 0
            end = pivot - 1
        } else{
            start = pivot
            end = nums.size -1
        }
        // print("search space = $start-$end")
        while(start <= end){
            var mid = start + (end - start) / 2
            if(nums[mid] == target){
                return mid
            } else if(nums[mid] < target){
                start = mid + 1
            } else{
                end = mid - 1
            }
        }
        return -1
    }
}
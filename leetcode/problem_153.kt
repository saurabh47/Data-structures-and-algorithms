// Problem 153. Find Minimum in Rotated Sorted Array (Medium)
// tags: Array, Binary Search
class Solution {
    fun findMin(nums: IntArray): Int {
        // [4,5,6,7,0,1,2]
        // 0            6
        var start = 0
        var end = nums.size -1

        if(nums[start] < nums[end]){
            return nums[start]
        }
        while(start < end){
            var mid = start + (end - start) / 2
            if(nums[mid] > nums[mid + 1]){
                return nums[mid + 1];
            }
            if(nums[mid - 1] > nums[mid]){
                return nums[mid];
            }
            if(nums[mid] > nums[start]){
                start = mid + 1
            } else if(nums[mid] < nums[start]){
                end = mid - 1
            }
        }
        return nums[start]
    }
}
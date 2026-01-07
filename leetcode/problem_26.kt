// Problem 26. Remove Duplicates from Sorted Array (Easy)
// tags: array, two pointers
class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var left = 0
        var index = 1
        // [0,1,2,3,1,2,2,3,3,4]
        for(right in 1..(nums.size - 1)){
            if(nums[left]<nums[right]){
                nums[index] = nums[right]
                index += 1
            }
            left += 1
        }
        return index
    }
}
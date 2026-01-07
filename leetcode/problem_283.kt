// Problem 283. Move Zeroes (Easy)
// tags: array, two pointers

class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        for(start in nums.indices){
            if(nums[start] != 0){
                continue
            }
            var end = start + 1
            while(end < nums.size && nums[end] == 0){
                end += 1
            }
            if(end >= nums.size){
                break
            }
            var t = nums[start]
            nums[start] = nums[end]
            nums[end] = t
        }
    }
}
/**
 * Problem 3024. Type of Triangle
 * tags: math
 * 
 */
class Solution {
    fun triangleType(nums: IntArray): String {
        if(nums[0] == nums[1] && nums[0] == nums[2]){
            return "equilateral"
        } else if((nums[0] + nums[1] <= nums[2]) || (nums[1] + nums[2] <= nums[0]) || (nums[0] + nums[2] <= nums[1])){
            return "none"
        } else if((nums[0] == nums[1]) || (nums[0] == nums[2]) || (nums[1] == nums[2])){
            return "isosceles"
        } else {
            return "scalene"
        }
    }
}
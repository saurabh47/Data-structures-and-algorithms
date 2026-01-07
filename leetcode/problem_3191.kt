// Problem 3191. Minimum Operations to Make Binary Array Elements Equal to One I (Medium)

class Solution {
    fun minOperations(nums: IntArray): Int {
        fun flip(index: Int){
            nums[index] = nums[index].xor(1)
        }
        var result: Int = 0;
        for(index in 0 until nums.size - 2){
            val num = nums[index]
            if(num == 0){
                flip(index)
                flip(index + 1)
                flip(index + 2)
                result += 1
            }     
        }
        // print(nums.joinToString())
        if(nums[nums.size - 1] <=0  || nums[nums.size - 2] <= 0){
            return -1;
        }
        return result;
    }
}
class Solution {
    fun firstMissingPositive(nums: IntArray): Int {
        // Our solution set is in range 1...nums.size + 1
        // so the idea is to loop through solution set and 
        // check if a num exists in the array in O(1)
        // by replacing num - 1 index with its negative equivalent
        // initially we will replace all -ves with 0
        // e.g nums = [3,4,-1,1]
        // make -ve to zero nums = [3,4,0,1]
        // index = nums[i] - 1 => 3 -1 => 2
        // nums[index] > 0 => make -ve
        // nums[index] == 0 => -nums.size [3 , 4, -4, 1]
        // nums[index] == 1 => -nums.size [3 , 4, -4, -1]
        // nums[index] == -4 => 4 -1 => 3 => -1 => -ve means
        //  we have already visited [3 , 4, -4, -1]

        val n = nums.size
        for(i in nums.indices){
            if(nums[i] < 0){
                nums[i] = 0
            }
        }

        // Modify array to be able to check in O(1) if i in 1..n exists
        // we use following rules num - 1 =>
        // num is +ve => make -ve
        //  -ve if its is +ve
        // 0 => - len(nums)
        // +ve => -ve
        for(i in nums.indices){
            val value = abs(nums[i])
            if(value >= 1 && value <= n){
                if(nums[value - 1] > 0){
                    nums[value - 1] *= -1
                } else if(nums[value - 1] == 0){
                    nums[value - 1] = -(n + 1)
                }
            }
        }
        for(i in 1..n){
            if(nums[i - 1] >= 0){
                return i
            }
        }
        return n + 1
    }
}
/**
 * Problem 238. Product of Array Except Self
 * tags: array, prefix sum
 */
// time complexity: Bruteforce O(n^2)
// space complexity: O(1)
class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        /*
        *  input: [1, 2, 3, 4, 5]
         * example: [1, 2, 6, 24, 120]
         */
        var result: IntArray = IntArray(nums.size){0}
        for( i in nums.indices){
            var product = 1
            for(j in nums.indices){
                if(i != j){
                    product *= nums[j]
                }
            }
            result[i] = product
        }
        return result  
    }
}


// time complexity: O(n)
// space complexity: O(n)
class OptimizedSolution {
    fun productExceptSelf(nums: IntArray): IntArray {
        /*
        *  input: [1, 2, 3, 4, 5]
         * example: [1, 2, 6, 24, 120]
         * 
         */
        var result: IntArray = IntArray(nums.size){0}
        var prefix: IntArray = IntArray(nums.size){0}
        var postfix: IntArray = IntArray(nums.size){0}
        var product = 1
        var postProduct = 1
        for(i in nums.indices){
            product *= nums[i]
            prefix[i] = product
            var j = (nums.size - 1) - i
            postProduct *= nums[j]
            postfix[j] = postProduct
        }
        for(i in nums.indices){
            if(i == 0){
                result[i] = postfix[i + 1]
            } else if(i == nums.size - 1){
                result[i] = prefix[i - 1]
            } else{
                result[i] = prefix[i-1] * postfix[i + 1]
            }
        }
        return result  
    }
}

// time complexity: O(n)
// space complexity: O(1)
class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        /*
        *  input: [1, 2, 3, 4, 5]
         * example: [1, 2, 6, 24, 120]
         * 
         */
        var result: IntArray = IntArray(nums.size){0}
        var product = 1
        // store prefix in the array
        for(i in nums.indices){
            result[i] = product
            product *= nums[i]
        }
        product = 1
        for(i in nums.size - 1 downTo 0){
            result[i] *= product
            product *= nums[i]
        }
        return result  
    }
}
// Problem 268. Missing Number (Easy)
// tags: array, hashtable, math binary search

// time complexity: O(n)
// space complexity: O(n)
class Solution {
    fun missingNumber(nums: IntArray): Int {
        var arr =  IntArray(nums.size + 1){-1}
        // [0, 1, 0, 3]
        for(i in nums){
            arr[i] = i
        }

        for(i in arr.indices){
            if(arr[i] == -1){
                return i
            }
        }
        return 0
    }
}

class Solution {
    fun missingNumber(nums: IntArray): Int {
        var n = nums.size
        var actual_sum = nums.sum()
        var expected_sum = (n * (n+1))/2
        return expected_sum - actual_sum
    }
}
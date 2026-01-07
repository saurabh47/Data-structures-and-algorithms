// Problem 448. Find All Numbers Disappeared in an Array (Easy)
// tags: array, hashtable
// time complexity: O(n)
// space complexity: O(n)
class Solution {
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        var arr = IntArray(nums.size + 1){0}
        // [4,3,2,7,8,2,3,1]
        // [0, 1, 2, 3, 4, 0, 0, 7, 8]
        for(i in nums){
            arr[i] = i
        }
        var result = mutableListOf<Int>()
        for(i in 1 until arr.size){
            if(arr[i] == 0){
                result.add(i)
            }
        }
        return result
    }
}
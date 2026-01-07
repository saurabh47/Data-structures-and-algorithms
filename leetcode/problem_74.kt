// Problem 74. Search a 2D Matrix (Medium)
// tags: Array, Binary Search
// time complexity: O(log(n))

class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        /*
        * input: give a 2d arr
        * task: find target
        *
        */ 
        var start = 0
        var end = matrix.size - 1
        while(start <= end){
            var mid = start + (end - start) / 2
            if(matrix[mid][0] == target){
                return true
            } else if(matrix[mid][0] > target){
                end = mid - 1
            }else{
                start = mid + 1
            }
        }
        if(start <= 0){
            return false
        }
        var row = start - 1
        start = 0
        end = matrix[row].size - 1
        while(start <= end){
            var mid = start + (end - start) / 2
            if(matrix[row][mid] == target){
                return true
            } else if(matrix[row][mid] > target){
                end = mid - 1
            }else{
                start = mid + 1
            }
        }
        return false
    }
}
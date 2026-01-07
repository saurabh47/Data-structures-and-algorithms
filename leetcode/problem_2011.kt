// Problem 2011. Final Value of Variable After Performing Operations (Easy)
// tags: Array, String
class Solution {
    fun finalValueAfterOperations(operations: Array<String>): Int {
        var count = 0
        for(operation in operations){
            if(operation == "X++" || operation == "++X"){
                count += 1
            }else {
                count -= 1
            }
        }
        return count
    }
}
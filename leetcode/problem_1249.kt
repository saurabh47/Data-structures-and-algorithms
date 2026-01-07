// Problem 1249. Minimum Remove to Make Valid Parentheses
// tags: Medium, Stack, String
class Solution {
    fun minRemoveToMakeValid(s: String): String {
        // if you see ( add
        // if you see ) and stack is empty then skip
        var result: String = "";
        val hashSet = hashSetOf<Int>()
        val stack = mutableListOf<Int>()
        for (index in s.indices) {
            if (s[index] == '(') {
                stack.add(index)
            } else if(s[index]== ')') {
                if (stack.size == 0) {
                    hashSet.add(index)
                } else {
                    stack.removeLast()
                }
            }
        }
        // stack could have unnecessary index of "(" after matching with ")"
        // add them to hashSet for deletion
        while(stack.size > 0){
           hashSet.add(stack.removeLast())
        }
        for(index in s.indices){
            if(!hashSet.contains(index)){
                result += s[index]
            }
        }
        return result
    }
}
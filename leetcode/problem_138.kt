/**
 * Problem 138. Copy List with Random Pointer
 * tags: Hash Table, Linked List
 * Example:
 * var ti = Node(5)
 * var v = ti.`val`
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var next: Node? = null
 *     var random: Node? = null
 * }
 */

 class Solution {
    fun copyRandomList(node: Node?): Node? {
        /*
         * input: 7->13->11->10->1->null
         * input: 7->
         * input: nul->13->11->10->1->null
         *{7: 8,}
         */
        if(node == null){
            return null
        }
        var curr = node
        var hashMap = hashMapOf<Node, Node>()
        while(curr != null){
            hashMap[curr] = Node(curr.`val`)
            curr = curr.next
        }
        curr = node
        while(curr != null){
            var newNode = hashMap[curr]
            newNode?.next = hashMap[curr.next]
            newNode?.random = hashMap[curr.random]
            curr = curr.next
        }
        return hashMap[node]
    }
}
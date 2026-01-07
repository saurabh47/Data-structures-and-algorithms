/**
 * Problem 23. Merge k Sorted Lists (Hard)
 * tags: Array, Linked List, Heap
 */
/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

 // time complexity: O(nlogk), n is the number of elements in the list
// space complexity: O(k) , k is the number of elements in the list
class Solution {
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        /**
        *   input: List<Node>
        *   output: head:List<Node>
        *   Example : [[2, 5, 7], [1, 2, 3], [3, 4, 7]]
        *           pq = [[1, 2 ,3], [2, 5, 7], [3, 4, 7]]
        *           pq = [[2 ,3], [2, 5, 7], [3, 4, 7]]
        *           
        *                   tail: [2]
        *                   head: [1, 2]
        *           
        */
        var priorityQ = PriorityQueue<ListNode>(compareBy {it.`val`})
        var head: ListNode? = null
        var tail: ListNode? = null
        for(node in lists){ // time complexity: O(k)
            if(node != null){
                priorityQ.add(node) // time complexity: O(logk)
            }
        }

        while(priorityQ.size > 0){  // time complexity for this loop: O(n)
            var pointer = priorityQ.poll()  // time complexity: O(logk)
            val temp = ListNode(pointer.`val`)
            if(head == null){
                head = temp
                tail = temp
            }else{
                tail?.next = temp
                tail = tail?.next
            }
            pointer = pointer.next
            if(pointer != null){
                priorityQ.add(pointer)  // time complexity: O(logk)
            }
        }
        return head
    }
}
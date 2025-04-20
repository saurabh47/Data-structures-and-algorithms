/**
 * Problem 21. Merge Two Sorted Lists (Easy)
 *  tags: Array, Linked List, Heap
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

//  Using heap is an overkill for this problem
// time complexity: O(nlogk), n is the number of elements in the list, k = 2
class Solution {
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        var pQ = PriorityQueue<ListNode>(compareBy {it.`val`})
        if(list1 != null){
            pQ.add(list1)
        }
        if(list2 != null){
            pQ.add(list2)
        }
        var head: ListNode? = null
        var tail: ListNode? = null
        while(pQ.size > 0){
            var smallest = pQ.poll()
            var temp = ListNode(smallest.`val`)
            if(head == null){
                head = temp
                tail = temp
            } else {
                tail?.next = temp
                tail = tail?.next
            }
            smallest = smallest.next
            if(smallest != null){
                pQ.add(smallest)
            }
        }
        return head
    }
}

/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution2 {
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        var head: ListNode? = null
        var tail: ListNode? = null
        var left = list1
        var right = list2
        if(left == null && right != null){
            return right
        }
        if(right == null && left != null){
            return left
        }
        while(left != null && right != null){
            lateinit var temp: ListNode
            if(left.`val` < right.`val`){
                temp = ListNode(left.`val`)
                left = left.next
            }else{
                temp = ListNode(right.`val`)
                right = right.next
            }
            if(head == null){
                head = temp
                tail = temp
            }else{
                tail?.next = temp
                tail = tail?.next
            }
            
        }
        if(left != null){
            tail?.next = left
            tail = tail?.next
        }
        if(right != null){
            tail?.next = right
            tail = tail?.next
        }
        return head
    }
}
### Problem 2058. Nodes Between Critical Points (Medium): https://leetcode.com/problems/nodes-between-critical-points/
### Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        c_points = []
        count = 0
        prev = head
        start = prev.next
        if(start.next is None):
            return [-1, -1]
        min_distance = 100000
        max_distance = -1
        # start index
        index = 1
        while(start.next):
            # check local minima
            if(prev.val > start.val and start.next.val > start.val):
                c_points.append(index)
            # check local maxima
            elif(prev.val < start.val and start.next.val < start.val):
                c_points.append(index)
            index += 1
            prev = start
            start = start.next

        if(len(c_points) > 1):
            max_distance = c_points[-1] - c_points[0]
            for i in range(len(c_points)-1):
                diff = abs(c_points[i] - c_points[i+1])
                if(diff < min_distance):
                    min_distance = diff
        else:
            min_distance = -1
        return [min_distance, max_distance]


### Optimized by calculating min max in same iteration

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_cp = -1
        prev_cp = -1
        prev = head
        start = prev.next
        if(start.next is None):
            return [-1, -1]
        min_distance = 100000
        max_distance = -1
        # start index
        index = 1
        while(start.next):
            # check if critical point
            if((prev.val > start.val and start.next.val > start.val) or (prev.val < start.val and start.next.val < start.val)):
                if(first_cp == -1):
                    first_cp = index   
                else:
                    if(index - prev_cp < min_distance):
                        min_distance = index - prev_cp
                    max_distance = index - first_cp
                prev_cp = index
            index += 1
            prev = start
            start = start.next

        if(prev_cp == -1 or min_distance == 100000):
            min_distance = -1
        return [min_distance, max_distance]
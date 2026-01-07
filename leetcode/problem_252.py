### problem 252. Meeting Rooms
### tags: Array, Sorting, heap

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        # [[0,30],[5,10],[15,20], [7,10],[2,4], [22, 28]]
        # 0        5       10       15      20      25       30
        # |---------------------------------------------------|
        #          |-------|
        #                           |-------|  |-----------|
        #            |-----| 
        #   |----|

        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            pstart, pend = intervals[i - 1]
            if(start < pend):
                return False
        return True
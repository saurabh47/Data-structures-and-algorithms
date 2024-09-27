### Problem 731. My Calendar II (Medium): https://leetcode.com/problems/my-calendar-ii/
### tags: array, binary-search, segment-tree, ordered-set
class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlapping = []

    def book(self, start: int, end: int) -> bool:
        for os, oe in self.overlapping:
            if(not (start >= oe or os >= end)):
                return False
        for s, e in self.events:
            if(not (start >= e or end <= s)):
                ostart = max(start, s)
                oend = min(end, e)
                self.overlapping.append((ostart, oend))
        self.events.append((start,end))
        return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
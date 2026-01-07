### Problem 56. Merge Intervals (Medium): https://leetcode.com/problems/merge-intervals/
### tags: array, sorting
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            pstart, pend = result[- 1]
            if(start <= pend):
                prev = [min(pstart, start), max(end, pend)]
                result[-1] = prev
            else:
                result.append(intervals[i])
        return result
    
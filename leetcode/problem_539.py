### Problem 539. Minimum Time Difference
### tags: array, math, string, sorting
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def toMinute(p1):
            time1 = p1.split(":")
            hr = int(time1[0])
            min = int(time1[1])
            return hr * 60 + min

        for i in range(len(timePoints)):
            timePoints[i] = "{}".format(toMinute(timePoints[i]))
        timePoints.sort(key = lambda x: int(x))

        min_diff = 24*60 - int(timePoints[-1]) + int(timePoints[0])

        for i in range(1,len(timePoints)):
            prev = int(timePoints[i-1])
            curr = int(timePoints[i])
            min_diff = min(abs(curr - prev), min_diff)
        return min_diff


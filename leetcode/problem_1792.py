### Problem 1792. Maximum Average Pass Ratio (Medium): https://leetcode.com/problems/maximum-average-pass-ratio/
# tags: heap, greedy

# hint: store max increase in a heap and add student to the class with the max increase
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        min_h = []
        for i in range(len(classes)):
            p, t = classes[i]
            increase = ((p + 1)/ (t + 1)) - (p / t)
            t = (-1 * increase, p, t)
            heapq.heappush(min_h, t)
        
        for student in range(extraStudents):
            percentage, p, t = heapq.heappop(min_h)
            p += 1
            t += 1
            increase = ((p + 1)/ (t + 1)) - (p / t)
            t = (-1* increase, p, t)
            heapq.heappush(min_h, t)

        result = 0
        for per, p, t in min_h:
            result += (p/t)
        return (result/len(classes))
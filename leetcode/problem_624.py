### Problem 624. Maximum Distance in Arrays (Easy): https://leetcode.com/problems/maximum-distance-in-arrays/

### tags: array

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_num = arrays[0][-1]
        min_num = arrays[0][0]
        result = 0
        for i in range(1, len(arrays)):
            arr = arrays[i]
            result = max(result, max(arr[-1] - min_num, max_num - arr[0]))
            if(arr[-1] > max_num):
                max_num = arr[-1]
            if(arr[0] < min_num):
                min_num = arr[0]
        return result
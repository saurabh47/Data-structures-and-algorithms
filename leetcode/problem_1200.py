### Problem 1200. Minimum Absolute Difference (Easy): https://leetcode.com/problems/minimum-absolute-difference/

### tags: array, sorting

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        left = 0
        result = []
        min_diff = 1000000
        for right in range(left + 1, len(arr)):
            diff = arr[right] - arr[left]
            min_diff = min(min_diff, diff)
            left += 1
        left = 0
        for right in range(left + 1, len(arr)):
            diff = arr[right] - arr[left]
            if(diff == min_diff):
                result.append([arr[left], arr[right]])
            left += 1
        return result
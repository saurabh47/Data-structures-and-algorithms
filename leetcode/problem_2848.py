### Problem 2848. Points That Intersect With Cars
### tags: array, hashtable, prefix sum
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # 0        5       10       15      20      25       30
        # |---------------------------------------------------|               
        #   1        6  
        #   |--------|
        #       3       8
        #       |-------|
        #                   10       15
        #                   |-------|
        #     2   5
        #     |---|
        #        4         10
        #        |---------|
        # [[3, 8], [4, 4], [9, 10], [9, 10]]

        arr = [0 for i in range(101)]
        result = 0
        for start, end in nums:
            for i in range(start, end + 1):
                arr[i] = 1
        for i in range(101):
            result += arr[i]
        return result
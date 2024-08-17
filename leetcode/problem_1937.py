### Problem 1937. Maximum Number of Points with Cost (Medium)
### Tags: Dynamic Programming

# https://www.youtube.com/watch?v=STEJHYc9rMw
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        left  = [0] * m
        right = [0] * m
        # dp[i][j] deontes max points gained at i,j
        dp = points[0]

        for row in range(1, len(points)):
            for col in range(m):
                if(col == 0):
                    left[col] = dp[col]
                else:
                    left[col] = max(left[col-1] - 1, dp[col])


            for col in range(m-1, -1, -1):
                if(col == m-1):
                    right[col] = dp[col]
                else:
                    right[col] = max(right[col+1] - 1, dp[col])

            for col in range(m):
                dp[col] = max(left[col], right[col]) + points[row][col]
        return max(dp)
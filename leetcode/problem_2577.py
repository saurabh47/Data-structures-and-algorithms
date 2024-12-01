# Similar to 2290 https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/

# hint: spend time (wait) with nearest neighbors if current time is less than neighbor cell
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        r, c = 0, 0
        if(min(grid[r][c + 1], grid[r + 1][c]) > 1):
            return -1
        min_heap = [(0, 0, 0)]
        visited = set()
        while(min_heap):
            t, r, c = heapq.heappop(min_heap)
            if(r == rows - 1 and c == cols - 1):
                return t
            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neighbors:
                if(nr >= 0 and nr < rows and nc >=0 and nc < cols and (nr, nc) not in visited):
                    wait = (abs(grid[nr][nc] - t) % 2) ^ 1
                    ntime = max(t + 1, grid[nr][nc] + wait)
                    heapq.heappush(min_heap, (ntime, nr, nc))
                    visited.add((nr, nc))
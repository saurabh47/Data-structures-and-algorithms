### Problem 2500. Delete Greatest Value in Each Row (Easy)
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        operations  = len(grid[0])
        total = 0
        isSorted = False
        while(operations > 0):
            max_num = 0
            for i in range(len(grid)):
                row = grid[i]
                if(not isSorted):
                    row = sorted(row)
                top = row.pop()
                max_num = max(max_num, top)
                grid[i] = row
                print("top:", top, row)
            total += max_num
            operations -= 1
            isSorted = True
        return total
 
class Solution2:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        operations  = len(grid[0])
        total = 0
        nested_heap = []
        # create a heap out of each row and store it in a list
        for i in range(len(grid)):
            row = grid[i]
            max_heap = []
            for num in row:
                heapq.heappush(max_heap, -num)
            nested_heap.append(max_heap)
        # pop the max element from each heap and add it to the total
        while(operations > 0):
            max_num = 0
            for i in range(len(nested_heap)):
                row = nested_heap[i]
                top = heapq.heappop(row) * -1
                max_num = max(max_num, top)
            total += max_num
            operations -= 1
        return total

# Sort each rown and then choose max among each column
class Solution3:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        for row in grid:
            row.sort()
        cols = len(grid[0])
        for i in range(cols - 1, -1, -1):
            max_col = 0
            for j in range(len(grid)):
                max_col = max(max_col, grid[j][i])
            result += max_col
        return result
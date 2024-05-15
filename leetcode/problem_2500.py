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
        for i in range(len(grid)):
            row = grid[i]
            max_heap = []
            for num in row:
                heapq.heappush(max_heap, -num)
            nested_heap.append(max_heap)

        while(operations > 0):
            max_num = 0
            for i in range(len(nested_heap)):
                row = nested_heap[i]
                top = heapq.heappop(row) * -1
                max_num = max(max_num, top)
            total += max_num
            operations -= 1
        return total
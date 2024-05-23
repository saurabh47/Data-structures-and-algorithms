### Minimum Cost of Ropes: https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1

class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        cost = 0
        heapq.heapify(arr)
        while(len(arr) > 1):
            popped = (heapq.heappop(arr) + heapq.heappop(arr))
            cost += popped
            heapq.heappush(arr, popped)
        return cost

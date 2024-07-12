### Problem 746. Min Cost Climbing Stairs (Easy)
### Tags: Dynamic Programming

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f(i): cost to reach at step i
        # f(0) => 0
        # f(1) => 0
        # Since we can start at either 0 or 1
        # f(2) => min(15 + 20, 20) = 20
        # f(n+1)=> min(f(n-1),f(n))
        # Bottom up Approach
        costs = [0, 0]
        for step in range(2, len(cost)+1):
            # [10, 15, 20, 24, 15] goal -> 5 = 39
            # f(0) -> 0  -> 1, 2
            # f(1) -> 0  -> 2 , 3
            # f(2) -> min(cost[0] + f(0), cost[1] + f(1)) => 10, 15 => 10
            # f(3) -> min(cost[1] + f(1), cost[2] + f(2)) -> (15 + 0, 10 + 10) => 15
            # f(4) -> min(cost[3] + f(3), cost[2] + f(2)) -> (24 + 15, 20 + 10) => 30
            # f(5) -> min(cost[4] + f(4), cost[3] + f(3)) -> (15 + 30, 24 + 15) => 39
            cost_step = min(cost[step-2] + costs[0],cost[step-1] + costs[1])
            costs[0] = costs[1]
            costs[1] = cost_step
        return costs[1]

# Extension : Print path of min Cost
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = [0, 0]
        path = [0, 0]
        for step in range(2, len(cost)+1):
            cost_step = min(cost[step-2] + costs[0],cost[step-1] + costs[1])
            if(cost[step-2] + costs[0] < (cost[step-1] + costs[1])):
               path.append(step - 2)
            else:
               path.append(step - 1)
            costs[0] = costs[1]
            costs[1] = cost_step
        print(path)
        return costs[1]


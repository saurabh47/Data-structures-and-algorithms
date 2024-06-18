### Problem 826. Most Profit Assigning Work (Medium)
### Tags: Two Pointers, Sorting

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        # d [68,35,52,47,86] => [35, 47, 52, 68, 86]
        # p [67,17,1,81,3]  => [17, 81, 1, 67, 3]
        # w[92,10,85,84,82] =>  [10, 82, 84, 85, 92]

        # 81 + 0 + 81 + 81 + 81 = 324

        p = [x for _, x in sorted(zip(difficulty, profit))]
        difficulty.sort()
        worker.sort()
        total = 0
        i = 0
        m = 0
        for w in worker:
            while(i < len(difficulty) and w >= difficulty[i]):
                pr = p[i]
                m = max(m, pr)
                i += 1
            total += m
        return total


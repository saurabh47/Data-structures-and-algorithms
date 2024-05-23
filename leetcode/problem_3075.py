### Problem 3075. Maximum Happiness Sum (Medium) 
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sorted_happiness = sorted(happiness)
        total_happiness = 0
        reduction = 0
        n = len(sorted_happiness)
        for i in range(n-1, n-k-1, -1):
            happy = sorted_happiness[i] - reduction
            total_happiness += max(happy, 0)
            reduction += 1
        # 1 2 3 4 5
        5, 3, 2, 1
        return total_happiness
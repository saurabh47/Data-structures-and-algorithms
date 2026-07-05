class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set(candyType)
        totalTypes = len(types)
        canEat = len(candyType) // 2
        return min(canEat, totalTypes)


if __name__ == "__main__":
    print(Solution().distributeCandies([1, 1, 2, 2, 3, 3]))
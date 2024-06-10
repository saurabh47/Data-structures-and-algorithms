### Problem 135. Candy (Hard) https://leetcode.com/problems/candy/
### Tags: [Array, Greedy]

### Similar to problem 42. Trapping Rain Water (Hard) https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = 0
        numberOfCandies = 1
        cdies = [1 for r in ratings]
        for i in range(len(ratings)):
            rating = ratings[i]
            if(i > 0):
                prev_rating = ratings[i-1]
                if(prev_rating < rating):
                    cdies[i] = cdies[i-1]+1
        for i in range(len(ratings) - 1, -1, -1):
            rating = ratings[i]
            if(i < len(ratings) - 1):
                next_rating = ratings[i+1]
                if(next_rating < ratings[i]):
                    cdies[i] = max(cdies[i], cdies[i+1] + 1)
            candies += cdies[i]
        return candies
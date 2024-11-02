### Problem 135. Candy (Hard) https://leetcode.com/problems/candy/
### Tags: [Array, Greedy]

# hint: satisfy left neighbour, right neighbour and return total
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

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if(ratings[i] > ratings[i-1]):
                candies[i] = candies[i-1] + 1
        total = candies[len(ratings)-1]
        for i in range(len(ratings)-2, -1, -1):
            if(ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]):
                candies[i] = candies[i+1] + 1
            total += candies[i]
        return total
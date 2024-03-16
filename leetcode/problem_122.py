# Problem 122. Best Time to Buy and Sell Stock II (Easy): https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# hint: add positive profits
class Solution:
    def maxProfit(self, prices) -> int:
        total = 0
        start = 0 
        end = 1
        if(len(prices) < 2):
            return total
        while(end < len(prices)):
            if(prices[end] - prices[start] > 0):
                total += (prices[end] - prices[start])
            start = end
            end += 1
        return total

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices)) # 7
    prices = [1,2,3,4,5]
    print(Solution().maxProfit(prices)) # 4
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices)) # 0
    prices = [1]
    print(Solution().maxProfit(prices)) # 0
    prices = [1,2]
    print(Solution().maxProfit(prices)) # 1
    prices = [1,2,3,4,5]
    print(Solution().maxProfit(prices)) # 4
    prices = [1,2,3,4,5,6]
    print(Solution().maxProfit(prices)) # 5
# Problem 121: Best Time to Buy and Sell Stock (Easy): https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = 0
        profit = 0
        while(sell_day < len(prices)):
            if(prices[sell_day] < prices[buy_day]):
                buy_day = sell_day
            if(prices[sell_day] - prices[buy_day] > profit):
                profit =  prices[sell_day] - prices[buy_day]
            sell_day+=1
        return profit

# Dynamic Programming

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # f(i) => j => max(prices[j]-prices[i]) or 0
        # [7,1,5,3,6,4]
        # day    MiB              MxP
        # f(0) -> 7, (0, 7 - 7) => 0
        # f(1) -> 1, (0, 1 - 1) => 0  
        # f(2) -> 1, (0, 5 - 1) => 4
        # f(3) -> 1, (4, 3 - 1) => 4
        # f(4) -> 1, (4, 6 - 1) => 5
        # f(5) -> 1, (5, 4 - 1) => 5
        max_profit = 0
        min_buy = prices[0]
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)
        return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices)) # 5

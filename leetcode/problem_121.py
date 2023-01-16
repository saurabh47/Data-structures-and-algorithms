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

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices)) # 5

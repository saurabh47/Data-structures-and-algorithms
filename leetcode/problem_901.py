### Problem 901. Online Stock Span (Medium): https://leetcode.com/problems/online-stock-span/
### tags: stack
class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        span = 1
        # [(100, 1), (80, 1), (70, 2), (60, 1), (75, 4), (85, )
        #   [1,    ,  1     ,  2     ,  1,   ,  4     ]
        while(self.stocks and self.stocks[-1][0] <= price):
            span += self.stocks[-1][1]
            self.stocks.pop()
        self.stocks.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
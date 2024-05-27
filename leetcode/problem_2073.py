### Problem 2073. Time Required to Buy N Tickets (Medium): https://leetcode.com/problems/time-required-to-buy-n-tickets/

### Tags: Array, Greedy

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            ticket = tickets[i]
            if(i <= k):
                time += min(ticket, tickets[k])
            else:
                if(ticket < tickets[k]):
                    time += ticket
                else:
                    time += (tickets[k] - 1)
        return time

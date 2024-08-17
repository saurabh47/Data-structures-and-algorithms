### Problem 1518. Water Bottles (Easy)

### Tags: Math
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        maxDrink = numBottles
        emptyBottles = 0
        while((numBottles // numExchange) > 0):
            maxDrink += (numBottles // numExchange)
            emptyBottles = numBottles % numExchange
            numBottles = (numBottles // numExchange)
            numBottles += emptyBottles 
        return maxDrink
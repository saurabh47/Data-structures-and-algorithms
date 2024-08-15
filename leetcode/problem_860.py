### Problem 860. Lemonade Change (Easy): https://leetcode.com/problems/lemonade-change/
### tags: array, greedy
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0
        for bill in bills:
            if(bill == 5):
                fives += 1
            elif(bill == 10):
                tens += 1
                if(fives > 0):
                    fives -= 1
                else:
                    return False
            elif(bill == 20):
                twenties += 1
                if(tens > 0 and fives > 0):
                    tens -= 1
                    fives -= 1
                elif(fives > 2):
                    fives -= 3
                else:
                    return False
        return True
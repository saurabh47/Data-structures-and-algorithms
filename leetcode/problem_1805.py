### Problem 1805. Number of Different Integers in a String
### tags: hashtable, string
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        def isDigit(char):
            return ord(char) >= 48 and ord(char) <= 57
        count = 0
        numbers = set()
        start = 0
        end = 0
        numStarted = False
        while(end != len(word)):
            char = word[end]
            if(isDigit(char)):
                if(start == end):
                    if(char == '0'):
                        if(end == len(word) - 1):
                            numStarted = True
                        elif(isDigit(word[end + 1])):
                            start += 1
                        else:
                            numStarted = True
                    else:
                        numStarted = True
                end += 1
            else:
                if(isDigit(word[start])):
                    numbers.add(word[start:end])
                    numStarted = False
                end += 1
                start = end
        # word ended
        if(numStarted):
            numbers.add(word[start:end])
        return len(numbers)
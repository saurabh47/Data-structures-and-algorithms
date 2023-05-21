# Problem 338. Counting Bits (Medium): https://leetcode.com/problems/counting-bits/
from pyparsing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for number in range(n+1):
            result.append(0)

        for number in range(n+1):
            target = number
            count = 0
            while(target !=0):
                if(target & 1 == 1):
                    count+=1
                target = target >> 1
            result[number] = count
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.countBits(5))
    print(solution.countBits(2))

### output
# mahesh@Maheshs-MacBook-Air-M1 bit-manipulation % python3 problem_338.py
# [0, 1, 1, 2, 1, 2]
# [0, 1, 1]



# Solution using dynamic programming
# We use the previous result to calculate the current result
# For example, if we have calculated the result for 1, we can use that to calculate the result for 5
class Solution2:
    def countBits(self, n: int) -> List[int]:
        result = []
        for number in range(n+1):
            if(number == 0):
                result.append(0)
            else:
                offset = 1 << int(floor(log(number, 2)))
                result.append(1 + result[number-offset])
        return result
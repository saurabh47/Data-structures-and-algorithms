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

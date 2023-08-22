# Given an integer variable n, find the first n odd powers of 3.
# eg: if n=3, output -> {3, 27, 243}.

class Solution:
    def powerOf(self, n:int, k:int):
        result = 1;
        while(k > 0):
             if(k & 1):
                 result = result*n
             n = n*n
             k = k >> 1
        return result;

    def findNOddPowers(self, n: int):
        result = []
        k = 1
        for i in range(n):
            result.append(self.powerOf(3,k));
            k+=2
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNOddPowers(5))

### Output
# mahesh@Maheshs-MacBook-Air-M1 bit-manipulation % python3 odd_powers.py
# [3, 27, 243, 2187, 19683]

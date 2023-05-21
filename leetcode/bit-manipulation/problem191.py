# Problem 191: Number of 1 Bits (Easy): https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n!=0):
            # if number is odd bitwise AND is 1
            if(n & 1 == 1):
                count+=1
            n = n >> 1
        return count


if __name__ == '__main__':
    solution = Solution()
    binary  = input("Enter a binary number:")
    print(solution.hammingWeight(int(binary,2)))

### output
# Enter a binary number:00000000101
# 2
# mahesh@Maheshs-MacBook-Air-M1 bit-manipulation % python3 problem1.py
# Enter a binary number:00000000000110101011
# 6

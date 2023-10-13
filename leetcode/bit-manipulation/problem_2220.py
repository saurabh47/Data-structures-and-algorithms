# Problem 2220. Minimum Bit Flips to Convert Number (Easy): https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR of two numbers will give 1 if the bits are different
        # XOR start and goal, and count the number of 1s
        target = start ^ goal;
        count = 0
        while(target!=0):
            # if number is odd, it means the last bit is 1
            if(target & 1 == 1):
                count += 1
            target = target >> 1
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.minBitFlips(2, 6)) # 1
    print(solution.minBitFlips(4, 7)) # 2

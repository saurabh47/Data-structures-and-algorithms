# Problem 268. Missing Number (Easy): https://leetcode.com/problems/missing-number/
from pyparsing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums);
        sum_exp = (length * (length+1)) >> 1
        sum_act=0
        for i in range(length):
            sum_act +=nums[i]
        return int(sum_exp - sum_act);


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([3,0,1]))
    print(solution.missingNumber([0,1]))
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))

### output
# mahesh@Maheshs-MacBook-Air-M1 bit-manipulation % python3 problem_268.py
# 2
# 2
# 8


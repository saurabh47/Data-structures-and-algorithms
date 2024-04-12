# Problem 1512. Number of Good Pairs (Easy): https://leetcode.com/problems/number-of-good-pairs/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gpairs = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] in gpairs:
                count += gpairs[nums[i]]
            else:
                gpairs[nums[i]] = 0
            gpairs[nums[i]] = gpairs[nums[i]] + 1
        return count

# Time Complexity: O(n)
# Space Complexity: O(n)

if __name__ == '__main__':
    s = Solution()
    print(s.numIdenticalPairs([1,2,3,1,1,3]))  # 4
    print(s.numIdenticalPairs([1,1,1,1]))  # 6
    print(s.numIdenticalPairs([1,2,3]))  # 0
    print(s.numIdenticalPairs([1,2,3,4,5,6,7,8,9,10]))  # 0
    print(s.numIdenticalPairs([1,1,1,1,1,1,1,1,1,1]))  # 45

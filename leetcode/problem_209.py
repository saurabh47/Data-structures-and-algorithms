### Problem 209. Minimum Size Subarray Sum
# hint:Two Pointers Technique like a snail
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        currentSum = 0
        end = 0
        start = end 
        while(end < len(nums)):
            currentSum += nums[end]
            while(currentSum >= target):
                minLen = min(minLen, end - start + 1)
                currentSum -=nums[start]
                start += 1
            end += 1
        if(minLen != float("inf")):
            return minLen
        return 0

# Time Complexity: O(n)
# Space Complexity: O(1)

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))  # 2
    print(s.minSubArrayLen(4, [1,4,4]))  # 1
    print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # 0
    print(s.minSubArrayLen(11, [1,2,3,4,5]))  # 3
    print(s.minSubArrayLen(11, [1,2,3,4,5,6]))  # 3
    print(s.minSubArrayLen(11, [1,2,3,4,5,6,7]))  # 3
    print(s.minSubArrayLen(11, [1,2,3,4,5,6,7,8]))  # 2
    print(s.minSubArrayLen(11, [1,2,3,4,5,6,7,8,9]))  # 1
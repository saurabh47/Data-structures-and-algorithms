### Problem: Given an unsorted integer array, find the smallest missing positive integer.
### Tags: [Array, Hash Table]

### Time Complexity: O(n)
### Space Complexity: O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
            if(smallest in h):
                smallest += 1
        while(smallest in h):
            smallest += 1
        return smallest

### Optimized Solution
### Time Complexity: O(n)
### Space Complexity: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # change negative values to 0
        for i in range(len(nums)):
            if(nums[i] < 0):
                nums[i] = 0

        # marks elements as -ve to indicate existence
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if(index >= 0 and index < len(nums)):
                # if not already marked
                if(nums[index] > 0):
                    nums[index] *= -1
                # mark values to a special value
                elif(nums[index] == 0):
                    nums[index] = -1 * (len(nums) + 1)

        smallest = 1
        for i in range(1, len(nums)+1):
            if(nums[i-1] >= 0):
                smallest  = i
                break
            else:
                smallest += 1
        return smallest
### Problem 945. Minimum Increment to Make Array Unique (Medium): https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
### Tags: Array, Hash Table, Sort

### Time Complexity: O(nlogn)
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        uniq = {}
        nums.sort()
        moves=0
        i = 0
        j = i+1
        while(j < len(nums)):
            if(nums[i] == nums[j]):
                nums[j] += 1
                moves += 1
            elif(nums[i] > nums[j]):
                diff = nums[i] - nums[j]
                nums[j] = nums[j] + diff + 1
                moves += (diff + 1) 
            i = j
            j+= 1
        return moves
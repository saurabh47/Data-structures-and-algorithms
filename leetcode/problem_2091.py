### Problem 2091. Minimum Deletions to Make Array Balanced (Medium)
### tags: array, greedy

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        # 1. find index of min and max in the array
        # 2. find the min elements to delete from front, back and ends of the array
        # 3. return the minimum of the three scores
        
        s, l = 0, 0  # index
        for i in range(len(nums)):
            smallest = nums[s]
            largest = nums[l]
            num = nums[i]
            if(num < smallest):
                s = i
            if(num > largest):
                l = i
        result = 0 

        front_score = max(s, l) + 1
        back_score = len(nums) - min(s, l)
        end_score = 0
        if(s <= l):
            end_score = (s+1) + (len(nums) - l)
        else:
            end_score = (l+1) + (len(nums) - s)
        return min(front_score, min(back_score, end_score))


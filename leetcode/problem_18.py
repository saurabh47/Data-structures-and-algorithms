#### Problem 18. 4 Sum
### tags: array, two-pointers, sorting


# hint: sort, fix first two pointers and run last two pointers
# time: O(n^3)
# memory: O(n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        result = []
        nums.sort()
        for i in range(len(nums)-3):
            if(i > 0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1, len(nums)-2):
                if(j > i+1 and nums[j]==nums[j-1]):
                    continue
                start = j + 1
                end = len(nums) - 1
                while(start < end):
                    curr_sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if(curr_sum == target):
                        result.append([nums[i], nums[j], nums[start], nums[end]])
                        while(start < end and nums[start]==nums[start+1]):
                            start += 1
                        while(start < end and nums[end]==nums[end-1]):
                            end -=1
                        start+=1
                        end -=1
                    elif(curr_sum > target):
                        end -=1
                    else:
                        start += 1
        return result
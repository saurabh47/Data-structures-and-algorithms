# Problem 15: 3Sum  (Medium): https://leetcode.com/problems/3sum/
# Tags: Array, Two Pointers
class Solution:
    def threeSum(self, nums):
        result = []
        target  = 0
        nums = sorted(nums)
        for i in range(len(nums)-2):
            k = len(nums)-1;
            j = i+1
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            while(j < k):
                sum_k = nums[i] + nums[j] + nums[k]
                if(sum_k < target):
                        j += 1
                elif(sum_k > target):
                        k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    result.append(temp)
                    while(j<k and nums[j] == nums[j+1]):
                        j+=1
                    while(j<k and nums[k] == nums[k-1]):
                        k-=1
                    j += 1
                    k -= 1 
        return result

# Time Complexity:  (O(n(logn) + n^2)) =  (O(n^2))
# Space Complexity: O(1)
# Similar to 4Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1,  1, 2]
        # 
        for i in range(len(nums) - 2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            start = i + 1
            end = len(nums) - 1
            while(start < end):
                s = nums[start] + nums[end] + nums[i]
                if(s == 0):
                    result.append([nums[start], nums[end], nums[i]])
                    while(start < end and nums[start]==nums[start+1]):
                        start += 1
                    while(end > start and nums[end]==nums[end - 1]):
                        end -= 1
                    start += 1
                    end -= 1
                elif(s < 0):
                    start += 1
                else:
                    end -= 1
        return result



# Time Complexity:  (O(n(logn) + n^2)) =  (O(n^2))
# Space Complexity: O(n)
# hint: sort and use two pointers
class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            # since array is sorted we can skip duplicates
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            start = i + 1
            end = len(nums) - 1
            while(start < end):
                sum3 = nums[i] + nums[start] + nums[end]
                if(sum3 < 0):
                    start += 1
                elif(sum3 > 0):
                    end -= 1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    # since array is sorted we can skip duplicates
                    while(nums[start] == nums[start - 1] and start < end):
                        start += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
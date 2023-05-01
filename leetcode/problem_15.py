# Problem 15: 3Sum  (Medium): https://leetcode.com/problems/3sum/
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

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
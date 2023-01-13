# Problem 238 (Medium): https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        product = 1
        result = []
        nonZeroProduct = 0
        zerocount = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                if(nonZeroProduct == 0):
                    nonZeroProduct = 1
                nonZeroProduct *=nums[i]
            else:
                zerocount+=1
            product *= nums[i]

        for i in range(len(nums)):
            if(nums[i] == 0):
                if(zerocount > 1):
                    result.append(product)
                else:
                    result.append(nonZeroProduct)
            else:
                result.append(product//nums[i])
        return result

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums)) # [24,12,8,6]
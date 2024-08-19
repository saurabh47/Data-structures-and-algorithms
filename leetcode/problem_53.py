# Problem 53: Maximum Subarray (Medium): https://leetcode.com/problems/maximum-subarray/ 

### Brute Force Solution
# Time Complexity: O(n^3)
class Solution1:
    def maxSubArray(self, nums):
        result = {}
        max_sum = -pow(10,4)
        length = len(nums)
        for size in range(1, length+1):
            if(size not in result):
                result[size] = []
            for i in range(length+1-size):
                temp = []
                start = i
                for j in range(i,i+size):
                    temp.append(nums[j])
                temp_sum = sum(temp)
                if(temp_sum > max_sum):
                    max_sum = temp_sum
                result[size].append(temp)
        return max_sum

# Brute Force Solution with Optimization
# Time Complexity: O(n^2)
class Solution2:
    def maxSubArray(self, nums):
        max_sum = -pow(10,4)
        for i in range(1, len(nums)):
            arr_sum = 0
            for j in range(len(nums)+1):
                if(i+j>len(nums)):
                    break
                arr_sum += nums[i+j-1]
                max_sum = max(max_sum, arr_sum)
                print('arr_sum: ', arr_sum, 'max_sum: ', max_sum)
        return max_sum

# Divide and Conquer Solution
# Time Complexity: O(nlogn)
class Solution3:
    def maxSubArray(self, nums):
        max_sum = -pow(10,4)
        length = len(nums)
        if(length==1):
            return nums[0]
        mid = length//2
        # print("mid=",mid)
        max_left = self.maxSubArray(nums[:mid])
        max_right = self.maxSubArray(nums[mid:])
        left_sum = -pow(10,4)
        temp_sum = 0
        for i in range(mid-1,-1,-1):
            temp_sum += nums[i]
            left_sum = max(left_sum,temp_sum)
        temp_sum = 0
        right_sum = -pow(10,4)
        for i in range(mid,length):
            temp_sum += nums[i]
            right_sum = max(right_sum,temp_sum)
        max_sum = max(max(max_left,max_right),left_sum+right_sum)
        return max_sum

# Kadane's Algorithm
# Time Complexity: O(n)
class Solution4:
    def maxSubArray(self, nums):
        max_sum = 0
        result = -pow(10,4)
        hasPositive = False
        for i in range(len(nums)):
            if(max_sum + nums[i] > 0):
                hasPositive = True
                max_sum += nums[i]
            else:
                max_sum = 0
            result = max(result, max_sum)
        if(not hasPositive):
            return max(nums)
        else:
            return result

class Solution5:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            curr_sum = max(curr_sum, 0)
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
        return max_sum

if __name__ == '__main__':
    s = Solution()
    # print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    # print(s.maxSubArray([-1]))
    print(s.maxSubArray([5,4,-1,7,8]))
# Problem 169. Majority Element (Easy): https://leetcode.com/problems/majority-element/
# hint: element with max freq will be the majority element

class Solution:
    def majorityElement(self, nums) -> int:
        freq = {}
        i = 0
        maxFreq = -1
        maxNum = 0
        while(i < len(nums)):
            if(nums[i] not in freq):
                freq[nums[i]] = 1
                # This should execute only once for both case [1, 2, 2, 3] and [1]
                if(maxFreq == -1):
                    maxNum = nums[i]
                    maxFreq = 1
            else:
                freq[nums[i]] += 1
                if(freq[nums[i]] > maxFreq):
                    maxFreq = freq[nums[i]]
                    maxNum = nums[i]
            i += 1
        return maxNum

if __name__ == "__main__":
    nums = [3,2,3]
    print(Solution().majorityElement(nums)) # 3
    nums = [2,2,1,1,1,2,2]
    print(Solution().majorityElement(nums)) # 2
    nums = [1]
    print(Solution().majorityElement(nums)) # 1

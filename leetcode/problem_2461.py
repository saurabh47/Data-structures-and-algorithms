#### Problem 2461. Maximum Subarray Sum with One Different Element
#### tags: array, sliding window, hashtable
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # input: k, arr
        # output: max sum of subarr of size k
        start = 0
        end = 0
        lookUp = defaultdict(int)
        s = 0
        result = 0
        # [1,2,4,2,9,9,9]
        while(end < len(nums)):
            s += nums[end]
            lookUp[nums[end]] += 1

            if((end - start + 1) > k):
                s -= nums[start]
                lookUp[nums[start]] -= 1
                if(lookUp[nums[start]] == 0):
                    lookUp.pop(nums[start])
                start += 1

            if(len(lookUp) == k and (end - start + 1) == k):
                result = max(s, result)
            end += 1
        return result
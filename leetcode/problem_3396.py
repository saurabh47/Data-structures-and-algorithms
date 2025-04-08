### Prob]em. 3396 Minimum Number of Operations to Make Elements in Array Distinct (Easy)
### tags: array, hash_map
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hm = {}
        for i in range(len(nums)):
            if(nums[i] not in hm):
                hm[nums[i]] = 1
            else:
                hm[nums[i]] += 1
        if(len(hm) == len(nums)):
            return 0
        # {1:1, 2:2, 3:3, 4:1, 5:1, 7:1}
        length = len(nums)
        start = 0
        count = 0
        # [1,2,3,4,2,3,3,5,7]
        while(start < len(nums)):
            if(length == len(hm)):
                return count
            if(start + 3 > len(nums)):
                return count + 1
            for i in range(start, start+3):
                hm[nums[i]] -= 1
                if(hm[nums[i]] == 0):
                    del hm[nums[i]]
                length -= 1
            start += 3
            count += 1
        return count

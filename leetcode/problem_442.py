### Problem 442. Find All Duplicates in an Array
### tags: Array, Hash Table

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        lookUp = Counter(nums)
        result = []
        for key, freq in lookUp.items():
            if(freq == 2):
                result.append(key)
        return result
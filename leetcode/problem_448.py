### Problem : 448. Find All Numbers Disappeared in an Array
### tags: Array, Hash Table
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lookUp = set()
        for num in nums:
            lookUp.add(num)
        
        result = []
        for i in range(1, (len(nums)) + 1):
            if(i not in lookUp):
                result.append(i)
        return result
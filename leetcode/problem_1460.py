### Problem 1460. Make Two Arrays Equal by Reversing Sub-arrays (Easy): https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

### Tags: Array, Hash Table
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if(len(target) != len(arr)):
            return False
        freq1 = Counter(target)
        freq2 = Counter(arr)
        for num in arr:
            if(num not in freq1 or (freq1[num] != freq2[num])):
                return False
        return True
### Problem 1636. Sort Array by Increasing Frequency (Easy): https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        def sort_num(num):
            return (freq[num], -num)
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        # nums.sort(key = sort_num)
        # sort based on the tuple if first parameter is same
        # uses second parameter -num to sort 
        nums.sort(key = lambda num: (freq[num], -num))
        return nums

# Time complexity: O(nlogn)
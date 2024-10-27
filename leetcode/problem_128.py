# Problem 128: Longest Consecutive Sequence (Medium): https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums) -> int:
        # Alternatively we can convert to set
        # and remove the duplicate check
        sortedlist = sorted(nums)
        start = 0
        result = []
        temp = []
        for end in range(len(sortedlist)):
            item = sortedlist[end]
            if(start != end):
                if(abs(item - sortedlist[end-1]) == 1):
                    temp.append(item)
                # Skip duplicate numbers
                # e.g 0 1 1 2
                elif(abs(item - sortedlist[end-1]) == 0):
                    continue
                else:
                    start = end
                    if(len(temp) > len(result)):
                        result = temp.copy()
                    temp.clear()
                    temp.append(item)
            else:
                temp.append(item)
        if(len(temp) > len(result)):
            result = temp.copy()
        return len(result)

#  Time Complexity: O(nlogn)
# space complexity: O(1)
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        count = 1
        if(len(nums) == 0):
            return 0
        for i, num in enumerate(nums):
            if((i != len(nums) - 1) and (num == nums[i + 1])):
                continue
            if((i != len(nums) - 1) and (num + 1 == nums[i + 1])):
                count += 1
            else:
                result = max(result, count)
                count = 1
        result = max(result, count)
        return result

#  Time Complexity: O(n)
# space complexity: O(n)
class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        result = 0
        for i, num in enumerate(s):
            if(num - 1 not in s):
                temp = num
                count = 0
                while(temp in s):
                    count += 1
                    temp += 1
            result = max(result, count)
        return result

if __name__ == "__main__":
    nums = [1,2 ,0, 1]
    print(Solution().longestConsecutive(nums)) # 4


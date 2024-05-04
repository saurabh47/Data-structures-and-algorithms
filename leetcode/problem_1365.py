# Problem 1365. How Many Numbers Are Smaller Than the Current Number (Easy): https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_numbers = sorted(nums)
        sm = {}
        result = []
        # 1, 2, 2, 3, 8
        for i in range(len(nums)):
            if(sorted_numbers[i] not in sm):
                sm[sorted_numbers[i]] = i

        for i in range(len(nums)):
            result.append(sm[nums[i]])
        return result

# Time complexity: O(nlogn)
# Space complexity: O(n)

if __name__ == '__main__':
    s = Solution()
    print(s.smallerNumbersThanCurrent([8,1,2,2,3])) # [4,0,1,1,3]
    print(s.smallerNumbersThanCurrent([6,5,4,8])) # [2,1,0,3]
    print(s.smallerNumbersThanCurrent([7,7,7,7])) # [0,0,0,0]
    print(s.smallerNumbersThanCurrent([1,2,3,4])) # [0,1,2,3]
    print(s.smallerNumbersThanCurrent([4,3,2,1])) # [3,2,1,0]
    print(s.smallerNumbersThanCurrent([1,1,1,1])) # [0,0,0,0]
    print(s.smallerNumbersThanCurrent([1,2,3,4,5,6,7,8,9])) # [0,1,2,3,4,5,6,7,8]
    print(s.smallerNumbersThanCurrent([9,8,7,6,5,4,3,2,1])) # [8,7,6,5,4,3,2,1,0]
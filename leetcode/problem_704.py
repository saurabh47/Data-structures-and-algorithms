# Problem 704. Binary Search
class Solution:
    def search(self, nums, target):
        return self.bSearch(nums, 0, len(nums) - 1, target)

    def bSearch(self, nums, start, end, target):
        mid = (start + end) // 2
        if(start > end):
            return  -1
        if(target == nums[mid]):
            return mid
        elif(target < nums[mid]):
            return self.bSearch(nums, start, mid-1, target)
        else:
            return self.bSearch(nums, mid + 1, end, target)

# Time Complexity: O(log n)
# Space Complexity: O(1)

if __name__ == '__main__':
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))  # 4
    print(s.search([-1,0,3,5,9,12], 2))  # -1
    print(s.search([5], 5))  # 0
    print(s.search([5], -5))  # -1
    print(s.search([5, 6], 6))  # 1
    print(s.search([5, 6], 5))  # 0
    print(s.search([5, 6], 7))  # -1
    print(s.search([5, 6, 7], 6))  # 1
    print(s.search([5, 6, 7], 5))  # 0
    print(s.search([5, 6, 7], 7))  # 2
    print(s.search([5, 6, 7], 8))  # -1
    print(s.search([5, 6, 7, 8], 6))  # 1
    print(s.search([5, 6, 7, 8], 5))  # 0
    print(s.search([5, 6, 7, 8], 7))  # 2
    print(s.search([5, 6, 7, 8], 8))  # 3
    print(s.search([5, 6, 7, 8], 9))  # -1
    print(s.search([5, 6, 7, 8, 9], 6))  # 1
    print(s.search([5, 6, 7, 8, 9], 5))  # 0
    print(s.search([5, 6, 7, 8, 9], 7))  # 2
    print(s.search([5, 6, 7, 8, 9], 8))  # 3
    print(s.search([5, 6, 7, 8, 9], 9))  # 4
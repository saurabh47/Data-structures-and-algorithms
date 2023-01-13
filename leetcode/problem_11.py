# Problem 11: Container With Most Water (Medium): https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height) -> int:
        max_area= 0 
        start = 0
        end = len(height) - 1
        while(start < end):
            width = end - start
            min_height = min(height[start], height[end])
            area = width*min_height
            if(area > max_area):
                max_area = area
            if(height[start] < height[end]):
                start+=1
            else:
                end-=1
        return max_area


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7])) # 49
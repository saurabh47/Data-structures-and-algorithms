### Problem 658. Find K Closest Elements (Medium): https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        size = len(arr)
        i = self.binSearch(arr, 0, size -1, x)
        p = i-1
        while(k > 0 and i < size and p >= 0):
            diff1 = abs(x - arr[p])
            diff2 = abs(x - arr[i])
            if(diff1 <= diff2):
                result.append(arr[p])
                p -= 1
            else:
                result.append(arr[i])
                i += 1
            k -= 1
        # one of the end has reached the end
        while(k > 0):
            if(p < 0):
                result.append(arr[i])
                i += 1
            elif(i >= size):
                result.append(arr[p])
                p -= 1
            k-=1
        return sorted(result)

    def binSearch(self, nums, start, end, target):
        if(nums[0] > target):
            return 0

        while(start <= end):
            mid = start + (end - start) //2
            print("searching start=",start, "end =", end, "mid=",mid)
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                end = mid-1
            else:
                start = mid+1
        return start


# Using heap (slow)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        for num in arr:
            pair = (abs(num - x), num)
            heapq.heappush(min_heap, pair)

        result = []
        for i in range(k):
            p = heapq.heappop(min_heap)
            result.append(p[1])
        return sorted(result)
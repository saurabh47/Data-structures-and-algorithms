# Problem 347: Top K Frequent Elements (Medium): https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums):
        freq = {}
        for i in range(len(nums)):
            num = nums[i]
            if(num not in freq):
                freq[num] = 1
            else:
                freq[num] += 1

        sorted_values = dict(sorted(freq.items(), key=lambda items: items[1],reverse=True))
        result = []
        for i, (key, value) in enumerate(sorted_values.items()):
            if(i < k):
                result.append(key)
            else:
                break;
        return result

class Solution2:
    def topKFrequent(self, nums, k: int):
        freq = {}
        result = []
        for num in nums:
            if(num in freq):
                freq[num] += 1
            else:
                freq[num] = 1
        priority_queue = []
        for key, value in freq.items():
            pair = (value, key)
            heapq.heappush(priority_queue, pair)

        most_freq = heapq.nlargest(k, priority_queue)
        for pair in most_freq:
            result.append(pair[1])
        return result

# Time complexity: O(nlogk), k is the number of most frequent elements
# Space complexity: O(n)
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result =[]
        min_heap = []
        for key, value in freq.items():
            pair = (value * -1, key)
            heapq.heappush(min_heap, pair)
        
        for i in range(k):
            value, key = heapq.heappop(min_heap)
            result.append(key)
        return result

# Time complexity: O(nlogn), n is the number of elements in the array
# Space complexity: O(n)
class Solution4:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = []
        output = []
        for keyy, v in freq.items():
            pair = (v, keyy)
            result.append(pair)
        result.sort(key = lambda x: -x[0])
        for num in result:
            if(k == 0):
                break
            output.append(num[1])
            k -= 1
        return output


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution2().topKFrequent(nums,k)) # [1,2]
# Problem 347: Top K Frequent Elements (Medium): https://leetcode.com/problems/top-k-frequent-elements/
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

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution2().topKFrequent(nums,k)) # [1,2]
# Problem 347: Top K Frequent Elements (Medium): https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums,k)) # [1,2]
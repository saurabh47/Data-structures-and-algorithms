### Problem 1310. XOR Queries of a Subarray
### tags: array, Prefix Sum, bit manipulation

# hint: XOR with same number is 0, order doesn't matter
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)
    
        answers = []
        for i in range(len(queries)):
            start, end = queries[i]
            res = prefix[end+1] ^ prefix[start]
            answers.append(res)
        return answers

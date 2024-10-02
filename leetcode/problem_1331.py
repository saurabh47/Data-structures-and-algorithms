### Problem 1331. Rank Transform of an Array (Easy)
### tags: array, hash table, sort
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedarr = sorted(arr)
        result = []
        rank = 1
        hash = {}
        for i in range(len(sortedarr)):
            curr = sortedarr[i]
            if(curr not in hash):
                hash[curr] = (1, rank)
                rank += 1
            else:
                freq, r = hash[curr]
                freq += 1
                hash[curr] = (freq, r)
        result = []
        for num in arr:
            result.append(hash[num][1])
        return result

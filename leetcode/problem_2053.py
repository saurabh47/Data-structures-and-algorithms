from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        uniq = [key for key in freq.keys() if(freq[key] == 1)]
        if(len(uniq) < k):
            return ''
        return uniq[k-1]
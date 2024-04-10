# Problem 274 : H-Index (https://leetcode.com/problems/h-index/)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hfreq = {}
        start = 0
        max_cit = 0
        min_cit = 1000
        length = len(citations)
        sorted_citations = sorted(citations)
        while(start < length):
            hfreq[sorted_citations[start]] = length - start
            start += 1
            while(start != length and sorted_citations[start - 1] == sorted_citations[start]):
                start += 1
        hMax = 0
        for key, value in hfreq.items():
            if min(key,value) >= hMax:
                hMax = min(key,value)
        return hMax

if __name__ == '__main__':
    s = Solution();
    result = s.hIndex([3,0,6,1,5]); #3
    print(result);
    result = s.hIndex([1,3,1]); #1
    print(result);
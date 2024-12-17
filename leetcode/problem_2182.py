### Problem 2182. Construct String With Repeat Limit (Medium): https://leetcode.com/problems/construct-string-with-repeat-limit/description

### tags:   [heap, greedy, string, counter]
# hint: Use heap to keep track of the frequency of the characters in the string.
# if freq exceeds limit then append 1 occurence of 2nd largest  and then add back remaining to heap
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_h = []
        for letter, value in freq.items():
            heapq.heappush(max_h, (ord(letter) * -1, value))
        result = []
        while(max_h):
            ascii, f = heapq.heappop(max_h)
            new_f = min(repeatLimit, f)
            result.append(new_f * chr(-ascii))
            if(f - new_f > 0 and max_h):
                ascii_2, f_2 = heapq.heappop(max_h)
                result.append(chr(-ascii_2))
                if(f_2 > 1):
                    heapq.heappush(max_h, (ascii_2, f_2 - 1))
                heapq.heappush(max_h, (ascii, f - new_f))
        return "".join(result)
### Problem 443. String Compression (Medium) https://leetcode.com/problems/string-compression/
# tags: string, two-pointers
class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        count = 0
        result = ''
        for i, curr in enumerate(chars):
            if(prev == curr):
                count += 1
            else:
                result +=prev
                if(count > 1):
                    result += str(count)
                prev = curr
                count = 1
        result +=prev
        if(count > 1):
            result += str(count)
        for i, char in enumerate(result):
            if(i >= len(chars)):
                chars.append(char)
            else:
                chars[i] = char
        # Pop extra chars
        while(len(result) < len(chars)):
            chars.pop()



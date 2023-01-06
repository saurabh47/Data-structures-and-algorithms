
# Problem 6: ZigZag Conversion (Medium): https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = {}
        factor = 1
        key = 0
        for i in range(len(s)):
            if(key not in result):
                result[key]=''
            print(key)
            result[key] += s[i]
            key = key + factor
            if(key>=(numRows-1) or key<= 0):
                factor = factor * -1
            print(result)
        result = ''.join(result.values())


if __name__ == '__main__':
    s = Solution()
    s.convert("PAYPALISHIRING", 3)


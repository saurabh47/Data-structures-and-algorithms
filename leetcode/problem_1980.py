#### Problem 1980. Find Unique Binary String
### tags: [array, hash-table, string, backtracking]
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def binToInt(s):
            x = 0
            pow = 0
            for i in range(len(s) -1, -1, -1):
                x += int(s[i]) * (2 ** pow)
                pow += 1
            return x

        def intToBin(x):
            res = ""
            while(x != 0):
                res += str(x % 2)
                x = x // 2
            return res[::-1]

        length = len(nums)
        maxNumbers = 2**length - 1
        s = set()
        for i in range(length):
            x = binToInt(nums[i])
            s.add(x)
        res = ""
        for i in range(2**length):
            if(i not in s):
                res = intToBin(i)
                break
        if(len(res) != length):
            res = "0" * (length - len(res)) + res
        return res
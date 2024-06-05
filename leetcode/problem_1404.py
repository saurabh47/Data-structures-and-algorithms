class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        num = self.binToNum(s)
        while(num != 1):
            # if odd
            if(num % 2 == 1):
                num += 1
            else:
                num = num >> 1
            count += 1
        return count

    def binToNum(self, s:str) -> int:
        num = 0
        for bit in s:
            num = (num << 1) | int(bit)
        return num


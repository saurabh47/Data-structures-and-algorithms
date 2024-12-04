class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index = 0
        i = 0
        res = ''
        while(index < len(spaces) and i < len(s)):
            if(i < spaces[index]):
                res += s[i]
                i += 1
            elif(i == spaces[index]):
                res += " "
                index += 1
        while(i < len(s)):
            res += s[i]
            i += 1
        return res
# Problem 14. Longest Common Prefix (Easy): https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs):
        matched = True
        result = ""
        index = 0
        k = 0
        smallestLength = 200
        for i in range(len(strs)):
            if(len(strs[i]) < smallestLength):
                smallestLength = len(strs[i])
                k = i
        if(smallestLength == 0):
            return result
        while(matched):
            toMatch = strs[k][index]
            for i in range(len(strs)):
                if(index < len(strs[i]) and strs[i][index] != toMatch):
                    matched = False
                    return result
            result += toMatch
            index += 1
            if(index >= smallestLength):
                break
        return result

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        result = ""
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if(first[i] != last[i]):
                return result
            result += first[i]
        return result

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs)) # "fl"
    strs = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs)) # ""
    strs = ["a"]
    print(Solution().longestCommonPrefix(strs)) # "a"
    strs = ["a","a"]
    print(Solution().longestCommonPrefix(strs)) # "a"
    strs = ["a","b"]
    print(Solution().longestCommonPrefix(strs)) # ""
    strs = ["a","ab"]
    print(Solution().longestCommonPrefix(strs)) # "a"
    strs = ["flowr","flowr","flow","flowesr"]
    print(Solution().longestCommonPrefix(strs)) # "flow"

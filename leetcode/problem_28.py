# Problem 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = 0
        if(len(needle) > len(haystack)):
            return -1
        index = 0
        while(end < len(haystack) and index < len(needle)):
            if(haystack[end] == needle[index]):
                print("match startes at",start, end,index)
                end += 1
                index += 1
            else:
                start += 1
                end = start
                index = 0
        if(index == len(needle)):
            return start
        else:
            return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("hello", "ll")) # 2
    print(solution.strStr("aaaaa", "bba")) # -1
    print(solution.strStr("aaaaa", "a")) # 0
    print(solution.strStr("mississippi", "issip")) # 4
    print(solution.strStr("mississippi", "issipi")) # -1
    print(solution.strStr("mississippi", "pi")) # 9
    print(solution.strStr("mississippi", "issi")) # 1
    print(solution.strStr("mississippi", "issis")) # -1
    
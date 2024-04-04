# Problem 58. Length of Last Word (Easy): https://leetcode.com/problems/length-of-last-word/

class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        k = len(s) - 1
        i = k
        while(s[k] == " " and k > 0):
            k -= 1

        if(k == 0):
            return 1
        else:
            i = k
            while(s[i] != " " and i > 0):
                i -= 1
            if(s[i] == " "):
                return k - i
            else:
                return k - i + 1


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        list = s.split(" ")
        for i in range(len(list) -1, -1, -1):
            if(len(list[i]) > 0):
                return len(list[i])

if __name__ == "__main__":
    s = "Hello World"
    print(Solution1().lengthOfLastWord(s)) # 5
    print(Solution2().lengthOfLastWord(s)) # 5
    s = "a"
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
    s = "a "
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
    s = " a"
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
    s = " "
    print(Solution1().lengthOfLastWord(s)) # 0
    print(Solution2().lengthOfLastWord(s)) # 0
    s = "a b"
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
    s = "a b c"
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
    s = "a b c "
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
    s = "a b c d"
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
    s = "a b c d e"
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
    s = "a b c d e f"
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
    s = "a b c d e f g"
    print(Solution1().lengthOfLastWord(s)) # 1
    print(Solution2().lengthOfLastWord(s)) # 1
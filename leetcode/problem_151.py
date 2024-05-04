class Solution:
    def reverseWords(self, s: str) -> str:
        stack =[]
        word = ''
        started = False
        for i in range(len(s)):
            if(s[i] != ' '):
                if(not started):
                    started = True
                word += s[i]
                if(i == len(s)-1):
                    stack.append(word)
                    started = False
            else:
                if(started):
                    stack.append(word)
                    word = ''
                    started = False
        result = ''
        for j in range(len(stack) - 1, -1, -1):
            result += stack[j]
            if(j != 0):
                result += ' '
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("the sky is blue")) # "blue is sky the"
    print(solution.reverseWords("  hello world!  ")) # "world! hello"
    print(solution.reverseWords("a good   example")) # "example good a"
    print(solution.reverseWords("  Bob    Loves  Alice   ")) # "Alice Loves Bob"
    print(solution.reverseWords("Alice does not even like bob")) # "bob like even not does Alice"
    
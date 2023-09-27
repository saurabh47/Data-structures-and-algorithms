# Problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for letter in s:
            if(len(stack) != 0):
                top = stack[-1]
                if letter == top:
                    stack.pop()
                else:
                    stack.append(letter)
            else:
                stack.append(letter)
        result = "".join(stack);
        return result;

if __name__ == '__main__':
    s = Solution();
    result = s.removeDuplicates('azxxzy');
    print(result);
    result = s.removeDuplicates('aabccba');
    print(result);
    result = s.removeDuplicates('aacbcca');
    print(result);

### output
# mahesh@Maheshs-MacBook-Air-M1 leetcode % python3 adjacent_duplicates.py
# ay
# a
# cba
# mahesh@Maheshs-MacBook-Air-M1 leetcode % 
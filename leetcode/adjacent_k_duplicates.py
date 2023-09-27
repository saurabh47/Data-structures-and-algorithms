# problem statement: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        result = []
        for letter in s:
            if len(result) == 0 or result[-1][0] != letter:
                result.append((letter,1))
            else:
                key = result[-1][0]
                value = result[-1][1]
                result.append((key,value+1))
                result.pop(-2)

            if(result[-1][1] == k):
               result.pop(-1)
            print(result);

        result_string ='';
        for key,value in result:
            result_string+=key*value
        return result_string

if __name__ == '__main__':
    s = Solution();
    result = s.removeDuplicates('ybggbbbbgssssgthyyyy',4); #ybth
    print(result);
    result = s.removeDuplicates('iiiixxxxxiiccccczzffffflllllllllfffffllyyyyyuuuuuz',5);#izzlz
    print(result);
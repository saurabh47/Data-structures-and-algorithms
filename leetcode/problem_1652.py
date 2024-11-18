### Problem 1652. Defuse the Bomb (Easy): https://leetcode.com/problems/defuse-the-bomb/
### tags: array, sliding window
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        if(k == 0):
            return result
        elif(k > 0):
            start = 0
            # [5, 7, 1, 4]
            #  s  e
            while(start != n):
                s = 0
                for end in range(start+1, start + k + 1):
                    index = end % n
                    s += code[index]
                # print("start=", start, "end=", end, "s=",s)
                result[start] = s
                start += 1
        else:

            end = n - 1
            # [5,6,13,12]
            while(end >= 0):
                s = 0
                for start in range(end - 1, end + k - 1, -1):
                    index = start % n
                    s += code[index]
                result[end] = s
                end -= 1
        return result

# Optimized solution
# Time complexity: O(n)
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        if(k == 0):
            return result
        start = 0
        s = 0
        for end in range(n + abs(k)):
            s += code[end % n]
            win_len = end - start + 1

            if(win_len > abs(k)):
                s -= code[start % n]
                start = (start + 1) % n
            
            win_len = end - start + 1
            if(win_len == abs(k)):
                if(k > 0):
                    result[(start - 1) % n] = s
                else:
                    result[(end + 1) % n] = s
        return result

### Problem 387. First Unique Character in a String (Easy): https://leetcode.com/problems/first-unique-character-in-a-string/
### Tags: Hash Table, String, Queue
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        q = []
        head = None
        # [love]
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = 1
                q.append(i)
            else:
                chars[s[i]] += 1
        for i in range(len(q)):
            if(chars[s[q[i]]] == 1):
                return q[i]
        return -1
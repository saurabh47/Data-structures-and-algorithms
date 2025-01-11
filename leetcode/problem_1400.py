#### Problem 1400: Construct K Palindrome Strings
### tags: String, Hash table
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if(k > len(s)):
            return False
        count = Counter(s)
        c = 0
        for kc, v in count.items():
            c += (v & 1)
        return (c <= k)
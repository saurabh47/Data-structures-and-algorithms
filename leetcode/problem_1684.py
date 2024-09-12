### Problem 1684. 
### tags: array, hash_table, string, bit manipulation, counting
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def isSetEqual(hash_1, hash_2):
            for k in hash_2:
                if(k not in hash_1):
                    return False
            return True

        hash_1 = set(allowed)
        count = 0
        for word in words:
            hash_2 = set(word)
            if(isSetEqual(hash_1, hash_2)):
                count += 1
        return count

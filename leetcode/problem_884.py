### Problem 884.Uncommon Words from Two Sentences
### tags: hashtable, string, counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result1 = Counter(s1.split())
        result2 = Counter(s2.split())
        print(result1, result2)
        result = set()
        for word, val in result1.items():
            if(word not in result2 and val == 1):
                result.add(word)
        for word,val in result2.items():
            if(word not in result1 and val == 1):
                result.add(word)
        return result
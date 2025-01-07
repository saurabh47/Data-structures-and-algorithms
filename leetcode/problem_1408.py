### probelem 1408. String Matching in an Array (Easy)
### tags: string, array
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if(i == j):
                    continue
                if(words[i] in words[j]):
                    result.append(words[i])
                    break
        return result
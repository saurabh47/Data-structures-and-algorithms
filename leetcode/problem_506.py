### Problem: 506. Relative Ranks (Easy): https://leetcode.com/problems/relative-ranks/
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = sorted(score,reverse = True)
        result = []
        index = {}
        for i in range(len(scores)):
            result.append("")
            index[scores[i]] = i
        for i in range(len(score)):
            if(index[score[i]] == 0):
                result[i] = "Gold Medal"
            elif(index[score[i]] == 1):
                result[i] = "Silver Medal"
            elif(index[score[i]] == 2):
                result[i] = "Bronze Medal"
            else:
                result[i] = str(index[score[i]] + 1)
        return result

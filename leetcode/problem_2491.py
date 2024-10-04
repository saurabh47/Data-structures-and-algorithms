### Problem 2491. Divide Players into Two Teams
### tags: two pointers, sorting
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s_skills = sorted(skill)
        start = 0
        end = len(s_skills) - 1
        res = s_skills[start] + s_skills[end]
        chemistry = 0
        while(end > start and res == (s_skills[start] + s_skills[end])):
            chemistry += (s_skills[start] * s_skills[end])
            start += 1
            end -= 1

        if(end < start):
            return chemistry
        return -1

### O(n) solution

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        pair_sum = (2 * sum(skill)) // len(skill)
        if(pair_sum == 0):
            return -1
        s_map = Counter(skill)
        chemistry = 0
        for key in skill:
            if(s_map[key] == 0):
                continue
            diff = pair_sum - key
            if(not s_map[diff]):
                return -1
            chemistry += (key * diff)
            s_map[diff] -= 1
            s_map[key] -= 1

        return chemistry

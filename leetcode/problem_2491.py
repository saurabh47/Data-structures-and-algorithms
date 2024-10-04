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
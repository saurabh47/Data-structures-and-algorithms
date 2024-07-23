### Problem 2418. Sort People by Height
### Tags: Array, Sorting
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = {}
        for i in range(len(heights)):
            height = heights[i]
            name = names[i]
            mapping[height] = name
        rev_heights = sorted(heights,reverse = True)
        result = []
        for i in range(len(rev_heights)):
            height = rev_heights[i]
            result.append(mapping[height])
        return result
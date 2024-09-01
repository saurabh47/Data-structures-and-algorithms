# Problem 2022: Convert 1D Array Into 2D Array (Medium)
# tags: array, matrix
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if(m * n != len(original)):
            return result
        i=0
        for row in range(m):
            r = []
            for col in range(n):
                r.append(original[i])
                i+=1
            result.append(r)
        return result
### Problem. 1380 Lucky Numbers in a Matrix
### tags: array, matrix

### Brute Force (O(M*N) * O(M+N)
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                element =  matrix[row][col]
                min_num = 100000
                max_num = 0
                for r in matrix[row]:
                    if(r < min_num):
                        min_num = r

                if(min_num == element):
                    for c in range(len(matrix)):
                        if(max_num < matrix[c][col]):
                            max_num = matrix[c][col]
                    if(min_num == max_num == element):
                        result.append(element)
        return result


### Optimized (O(M,N))

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = [100000 for i in range(len(matrix))]
        max_col = [0 for i in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                element =  matrix[row][col]
                if(element < min_row[row]):
                    min_row[row] = element
                if(element > max_col[col]):
                    max_col[col] = element
        
        result = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                element =  matrix[row][col]
                if(min_row[row] == max_col[col] and max_col[col] == element):
                    result.append(element)
        return result
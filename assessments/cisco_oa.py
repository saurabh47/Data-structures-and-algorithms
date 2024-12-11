'''
Lucy loves to play the Hop, Skip and Jump game. Given an N*M matrix and starting from cell (1,1), her challenge is to hop in an anti-clockwise direction and skip alternate cells. The goal is to find out the last cell she would hop onto.
Write an algorithm to find the last cell Lucy would hop onto after moving anti-clockwise and skipping alternate cells.

Input:

The first line of input consists of two integers- matrix_row and matrix_col, representing the number of rows (N) and the number of columns (M) in the matrix, respectively.
The next M lines consist of N space-separated integers representing the elements in each cell of the matrix.
Output
Print an integer representing the last cell Lucy would hop onto after following the given instructions.

Example
Input:

33
29 8 37
15 41 3
1 10 14
Output:
41

Explanation:
Lucy starts with 29, skips 15, hops onto 1, skip 10, hops onto 14, skips 3, hops onto 37, skips 8 and finally hops onto 41.
So, the output is 41.
'''

def funcHopSkipJump(matrix):
	directions  = [[0, 1], [1, 0], [0, -1], [-1, 0]]
	rows = len(matrix)
	cols = len(matrix[0])
	visited  = [[False for i in range(cols)] for j in range(rows)]
	direction = 1
	r, c = 0, 0
	if not matrix:
		return result
	hopCount = 0
	result = matrix[0][0]
	for _ in range(rows * cols):
		if(hopCount % 2 == 0):
			result = matrix[r][c]
		hopCount += 1
		visited[r][c] = True
		dr, dc = directions[direction]
		new_r, new_c = r + dr, c + dc
		if((new_r  >= rows) or (new_r < 0) or (new_c < 0) or (new_c >= cols) or (visited[new_r][new_c])):
			direction = (direction - 1) % 4
			dr, dc = directions[direction]
			new_r, new_c = r + dr, c + dc
		r , c = new_r, new_c
	return result
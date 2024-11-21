# GRAPHS

#             5
#           /   \
#         /       \
#        1---------2 
#        |         | \
#        |         |  \
#        |         |    \
#        4---------3-----7
#        |         |    /
#        |         |   /
#        |         |  /
#        |         | /
#        6---------1 
# 5-1,1-2,5-2,1-4,2-3,3-4,2-7,3-7,4-6,3-1,6-1,7-2,1-7          
# Adjacency Matrix
#      1  2  3  4  5  6  7
# ----------------------------
#  1 | 0  1  0  1  1  0  0 
#  2 | 1  0  1  0  1  0  1 
#  3 | 1  0  0  1  0  0  1 
#  4 | 1  0  1  0  0  1  0 
#  5 | 1  1  0  0  0  0  0 
#  6 | 1  0  0  1  0  0  0 
#  7 | 1  1  1  0  0  0  0 
# 
# 

if __name__ == "__main__":
  # input from the user
  vertices = set([int(node) for node in input("Enter no of nodes (separated by comma):").split(',')])
  length = len(vertices)
  
  matrix = [[0 for x in range(length)] for y in range(length)]
  edges = input("Enter edges between vertices seperated by comma e.g 1-2,2-3 :").split(',')
  print("edges=", edges)
  for edge in edges:
    a, b = edge.split('-')
    if(int(a) not in vertices or int(b) not in vertices):
      print("Invalid connections:", a, b)
      break
    matrix[int(a)-1][int(b)-1] = 1
    matrix[int(b)-1][int(a)-1] = 1
  
  print("Adjacency Matrix")
  print("    ", end="")
  for node in vertices:
    print(node, end="  ")
  print()
  print("----------------------------")
  for i in range(length):
    print(i+1, "|", end=" ")
    for j in range(length):
      print(matrix[i][j], end="  ")
    print()
# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no of the vertices "nodes"
class Graph:
  def __init__(self, size, directed):
    self.nodes_len = size
    self.roots = {}
    self.directed = directed

  # connects node a and b
  def addEdge(self, a, b):
    if a not in self.roots:
      self.roots[a] = []
    if b not in self.roots:
      self.roots[b] = []

    self.roots[a].append(b)
    if self.directed == False:
      self.roots[b].append(a)

  def showGraph(self):
    for key, values in self.roots.items():
      print("Current Vertex at: {}".format(key))
      for i in range(len(values)):
        print("Vertex {}".format(values[i]))

  def bfs_traversal(self, source):
    print("source node={}".format(source))
    toVisit=[source]
    visited = []
    while(len(toVisit)!=0):
      top = toVisit[0]
      for node in self.roots[top]:
        if node not in toVisit and node not in visited:
          toVisit.append(node)
      visited.append(top)
      toVisit.pop(0)
    print(visited)

#
#       1 ----- 3 -- -- 0
#     / |     / |     / |
#   /   |    /  |    /  |
# 5     |   /   |   /   |
#   \   |  /    |  /    |
#     \ | /     | /     |
#       2 ----- 4 -- -- 6
#

if __name__ == "__main__":
  # graph with 4 nodes and directed = False
  graph = Graph(7, False)
  graph.addEdge(5, 1)
  graph.addEdge(5, 2)
  graph.addEdge(2, 3)
  graph.addEdge(1, 2)
  graph.addEdge(1, 3)
  graph.addEdge(2, 3)
  graph.addEdge(2, 4)
  graph.addEdge(3, 4)
  graph.addEdge(3, 0)
  graph.addEdge(4, 0)
  graph.addEdge(4, 6)
  graph.addEdge(0, 6)
  print(graph.bfs_traversal(2))


### output
# mahesh@Maheshs-MacBook-Air-M1 graphs % python3 bfs.py
# source node=3
# [3, 2, 1, 4, 0, 5, 6]
# None
# mahesh@Maheshs-MacBook-Air-M1 graphs % python3 bfs.py
# source node=0
# [0, 3, 4, 6, 2, 1, 5]
# None
# mahesh@Maheshs-MacBook-Air-M1 graphs % python3 bfs.py
# source node=5
# [5, 1, 2, 3, 4, 0, 6]
# None
# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no of the vertices "nodes"

class Graph:
  def __init__(self, size, directed):
    self.nodes_len = size
    self.roots = {}
    self.directed = directed

  # connects node a and b
  def addEdge(self, a, b):
    # index_a = self.nodes.index(a)
    # index_b = self.nodes.index(b)
    if a not in self.roots:
      self.roots[a] = []
    if b not in self.roots:
      self.roots[b] = []

    self.roots[a].append(b)
    if self.directed == True:
      self.roots[b].append(a)

  def showGraph(self):
    for key, values in self.roots.items():
      print("Current Vertex at: {}".format(key))
      for i in range(len(values)):
        print("Vertex {}".format(values[i]))

#
# 3 - - 4
# |    /
# |   /
# |  /
# | /
#  2 -- -- 3
#

if __name__ == "__main__":
  # graph with 4 nodes and directed = False
  graph = Graph(4, False)
  graph.addEdge(3, 4)
  graph.addEdge(3, 7)
  graph.addEdge(4, 7)
  graph.addEdge(7, 8)
  print(graph.showGraph())

### Output ###

# Current Vertex at: 3
# Vertex 4
# Vertex 7
# Current Vertex at: 4
# Vertex 3
# Vertex 7
# Current Vertex at: 7
# Vertex 3
# Vertex 4
# Vertex 8
# Current Vertex at: 8
# Vertex 7
# None
# 
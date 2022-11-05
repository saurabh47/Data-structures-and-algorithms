# A class to represent the structure of a node in the graph
class Node:
  def __init__(self, data):
    self.vertex = data
    self.next = None

# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no of the vertices "nodes"

class Graph:
  def __init__(self, size):
    self.nodes = size
    self.roots = [None] * self.nodes

  # connects node a and b
  def addNode(self, a, b):
    node_a = Node(a)
    node_a.next = self.roots[b]
    self.roots[b] = node_a

    node_b = Node(b)
    node_b.next = self.roots[a]
    self.roots[a] = node_b

  def showGraph(self):
    for index in range(self.nodes):
      print("Current Vertex at: {}".format(index))
      root = self.roots[index]
      while (root):
        print("Vertex {}".format(root.vertex))
        root = root.next

#
# 0 - - 1
# |  /
# | /
# 2 - - 3
# 
if __name__ == "__main__":
  graph = Graph(4)
  graph.addNode(0, 1)
  graph.addNode(0, 2)
  graph.addNode(1, 2)
  graph.addNode(2, 3)
  print(graph.showGraph())



### output
# python3 adjacency_list.py
# Current Vertex at: 0
# Vertex 2
# Vertex 1
# Current Vertex at: 1
# Vertex 2
# Vertex 0
# Current Vertex at: 2
# Vertex 3
# Vertex 1
# Vertex 0
# Current Vertex at: 3
# Vertex 2
# None
# A class to represent the structure of a node in the graph
class Node:
  def __init__(self, data):
    self.vertex = data
    self.next = None

# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no of the vertices "nodes"

class Graph:
  def __init__(self, size, nodes):
    self.nodes_len = size
    self.nodes = nodes
    self.roots = [None] * self.nodes_len

  # connects node a and b
  def addNode(self, a, b):
    index_a= self.nodes.index(a)
    index_b= self.nodes.index(b)
    node_a = Node(a)
    node_a.next = self.roots[index_b]
    self.roots[index_b] = node_a

    node_b = Node(b)
    node_b.next = self.roots[index_a]
    self.roots[index_a] = node_b

  def showGraph(self):
    for index in range(self.nodes_len):
      print("Current Vertex at: {}".format(self.nodes[index]))
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
  graph = Graph(4, [3, 4, 7, 8])

  graph.addNode(3, 4)
  graph.addNode(3, 7)
  graph.addNode(4, 7)
  graph.addNode(7, 8)
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
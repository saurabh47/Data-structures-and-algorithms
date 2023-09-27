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

  def isConnected(self, source, destination, visited):
    if(source not in self.roots or destination not in self.roots):
        return False
    connections = self.roots[source]
    if(destination in connections):
        return True
    for connection in connections:
        if(connection not in visited):
            source = connection
            visited.append(connection)
            connected = self.isConnected(source, destination, visited)
            if(connected):
                return connected
    return False

  def showGraph(self):
    for key, values in self.roots.items():
      print("Current Vertex at: {}".format(key))
      for i in range(len(values)):
        print("Vertex {}".format(values[i]))

# {0: [1], 1: [0]}
# {0: [1], 1: [0, 2], 2: [1]}
# {0: [1, 2], 1: [0, 2], 2: [1, 0]}
# {0: [1, 2], 1: [0, 2, 3], 2: [1, 0], 3: [1]}
# {0: [1, 2], 1: [0, 2, 3], 2: [1, 0], 3: [1, 4], 4: [3]}
# {0: [1, 2], 1: [0, 2, 3], 2: [1, 0, 4], 3: [1, 4], 4: [3, 2]}
# {0: [1, 2], 1: [0, 2, 3], 2: [1, 0, 4, 3], 3: [1, 4, 2], 4: [3, 2]}

#
#       1 ----- 3
#     / |     / |
#   /   |    /  |
# 0     |   /   |
#   \   |  /    |
#     \ | /     |
#       2 ----- 4
#

if __name__ == "__main__":
  # graph with 5 nodes and directed = False
  graph = Graph(5, False)
  graph.addEdge(0, 1)
  graph.addEdge(1, 2)
  graph.addEdge(2, 0)
  graph.addEdge(1, 3)
  graph.addEdge(3, 4)
  graph.addEdge(2, 4)
  graph.addEdge(2, 3)
  graph.showGraph()
  print(graph.isConnected(0, 6, [])) # False

### Output ###

# mahesh@Maheshs-MacBook-Air-M1 graphs % python3 adjacency_list.py 
# Current Vertex at: 0
# Vertex 1
# Vertex 2
# Current Vertex at: 1
# Vertex 0
# Vertex 2
# Vertex 3
# Current Vertex at: 2
# Vertex 1
# Vertex 0
# Vertex 4
# Vertex 3
# Current Vertex at: 3
# Vertex 1
# Vertex 4
# Vertex 2
# Current Vertex at: 4
# Vertex 3
# Vertex 2
# None

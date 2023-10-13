import math
# A class to represent a weighted graph. A graph is represented as the list of the adjacency lists.
# The addEdge method has a optional weight parameter weight defaults to 1
# Size of the array will be the no of the vertices "nodes"
class Graph:
  def __init__(self, size, directed):
    self.nodes_len = size
    self.roots = {}
    self.nodes = {}
    self.distance_matrix = []
    for i in range(size):
            self.distance_matrix.append([0 for i in range(size)])
    self.directed = directed

  # connects node a and b with a weight of 1 by default
  def addEdge(self, a, b, weight=1):
    if a not in self.roots:
      self.roots[a] = []
    if b not in self.roots:
      self.roots[b] = []

    self.roots[a].append((b,weight))
    if self.directed == False:
      self.roots[b].append((a,weight))

  # adds a node at X,Y
  # and also adds a direct edge to all other nodes
  # by calculating the euclidean distance
  def addNode(self, a, x, y):
    if a not in self.roots:
      self.nodes[a]= (x,y)
      for key, values in self.nodes.items():
        if key != a:
          distance = self.distance(a, key)
          self.addEdge(a, key,distance)
          # self.update_distance_matrix(a, key, distance)


  # not being used since it costs to find index of a node based on its name
  def update_distance_matrix(self, a, b, distance):
    index_a = self.getVertices().index(a)
    index_b = self.getVertices().index(b)
    self.distance_matrix[index_a][index_b] = distance
    self.distance_matrix[index_b][index_a] = distance

  # euclidean distance between two nodes
  def distance(self, a, b):
    X1 = self.nodes[a][0]
    X2 = self.nodes[b][0]
    Y1 = self.nodes[a][1]
    Y2 = self.nodes[b][1]
    distance = math.sqrt((X1-X2)**2 + (Y1-Y2)**2)
    return round(distance,2)

  def getVertices(self):
    return list(self.roots.keys())

  # e.g PATH IS CAEDB 
  def getPathCost(self, path):
    cost = 0
    for i in range(len(path)-1):
        cost += self.distance(path[i], path[i+1])
    return cost

  def showGraph(self):
    for key, values in self.roots.items():
      print("City {}".format(key))
      for i in range(len(values)):
        print("connected to City {} at distance of {} units".format(values[i][0],values[i][1]))

# {
# 'A': [('X', 100), ('Y', 300)],
# 'X': [('A', 100), ('B', 200), ('C', 300), ('D', 500), ('E', 700), ('F', 900), ('G', 800),
# ('H', 600), ('I', 350), ('J', 270)],
# 'Y': [('A', 300), ('B', 130), ('C', 500), ('D', 390), ('E', 300), ('F', 600), ('G', 950), ('H', 560), ('I', 550), ('J', 350)],
# 'B': [('X', 200), ('Y', 130)],
# 'C': [('X', 300), ('Y', 500)],
# 'D': [('X', 500), ('Y', 390)],
# 'E': [('X', 700), ('Y', 300)],
# 'F': [('X', 900), ('Y', 600)],
# 'G': [('X', 800), ('Y', 950)],
# 'H': [('X', 600), ('Y', 560)],
# 'I': [('X', 350), ('Y', 550)],
# 'J': [('X', 270), ('Y', 350)]
# }


if __name__ == "__main__":
  # graph with 10 nodes and directed = False
  graph = Graph(5, False)
  graph.addNode('A', 100, 300)
  graph.addNode('B', 200,130)
  graph.addNode('C', 300,500)
  graph.addNode('D', 500, 390)
  graph.addNode('E', 700, 300)
  graph.addNode('F', 900, 600)
  graph.addNode('G', 800, 950)
  graph.addNode('H', 600, 560)
  graph.addNode('I', 350, 550)
  graph.addNode('J', 270, 350)
  graph.showGraph();
  print(graph.getPathCost('CEFHDJABIG'))



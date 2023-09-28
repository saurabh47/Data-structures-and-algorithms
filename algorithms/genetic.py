import numpy as np
import math

class Graph:
  def __init__(self, size, directed):
    self.nodes_len = size
    self.roots = {}
    self.nodes = {}
    self.directed = directed

  # connects node a and b
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

  # euclidean distance between two nodes
  def distance(self, a, b):
    X1 = self.nodes[a][0]
    X2 = self.nodes[b][0]
    Y1 = self.nodes[a][1]
    Y2 = self.nodes[b][1]
    distance = math.sqrt((X1-X2)**2 + (Y1-Y2)**2)
    return round(distance,2)

  def vertices(self):
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

class GeneticAlgorithmTSP:

    def __init__(self, generations=50, population_size=10, tournamentSize=4, mutationRate=0.1, fit_selection_rate=0.1):
        # the number of routes in each generation
        self.population_size = population_size
        # the number of generations to run the algorithm for
        self.generations = generations
        self.tournamentSize = tournamentSize
        self.mutationRate = mutationRate
        # The number of fittest routes to carry over to the next generation
        self.fit_selection_rate = fit_selection_rate

    def minCostIndex(self, costs):
       index = 0
       for i in range(len(costs)):
            if costs[i] < costs[index]:
                index = i
       return index

    def findFittestPath(self, graph):
        population = self.randomizeCities(graph.vertices())
        # the number of fittest routes to carry over to the next generation
        number_of_fits_to_carryover = math.ceil(self.population_size * self.fit_selection_rate)

        if (number_of_fits_to_carryover > self.population_size):
            raise ValueError('fitness Rate must be in [0,1].')

        print ('Optimizing TSP Route for Graph:\n{0}'.format(graph))

        for generation in range(self.generations):
            print ('\nGeneration: {0}'.format(generation + 1))
            print ('Population: {0}'.format(population))

            newPopulation = []
            fitness = self.computeFitness(graph, population)
            print ('Fitness: {0}'.format(fitness))
            fitIndex = self.minCostIndex(fitness)
            print ('Fittest Route: {0} fitness(minium cost): ({1})'.format(population[fitIndex], fitness[fitIndex]))

            if number_of_fits_to_carryover:
                fitPopulation = np.array(fitness).argsort()[:number_of_fits_to_carryover]
                [newPopulation.append(population[i]) for i in fitPopulation]
            for gen in range(number_of_fits_to_carryover, self.population_size):
                parent1 = self.__tournamentSelection(graph, population)
                parent2 = self.__tournamentSelection(graph, population)
                offspring = self.__crossover(parent1, parent2)
                newPopulation.append(offspring)
                # print ('\nParent 1: {0}'.format(parent1))
                # print ('Parent 2: {0}'.format(parent2))
                # print ('Offspring: {0}\n'.format(offspring))
            for gen in range(number_of_fits_to_carryover, self.population_size):
                newPopulation[gen] = self.__mutate(newPopulation[gen])

            population = newPopulation

            if self.__converged(population):
                print ('\nConverged to a local minima.', end='')
                break

        return (population[fitIndex], fitness[fitIndex])


    def randomizeCities(self, graph_nodes):
        # remove A from the list of nodes
        nodes = [node for node in graph_nodes if node != 'A']
        randomized = np.random.permutation(nodes)
        # add A as the first and last city
        randomized = np.insert(randomized, 0, 'A')
        randomized = np.append(randomized, 'A')
        return [''.join(v for v in randomized) for i in range(self.population_size)]

    # Fitness is the cost of the path
    # lower the cost, higher the fitness
    def computeFitness(self, graph, population):
        fitness = []
        for path in population:
            fitness.append(graph.getPathCost(path))
        return fitness


    def __tournamentSelection(self, graph, population):
        tournament_contestants = np.random.choice(population, size=self.tournamentSize)
        # print (tournament_contestants)
        tournament_contestants_fitness = self.computeFitness(graph, tournament_contestants)
        return tournament_contestants[np.argmin(tournament_contestants_fitness)]


    def __crossover(self, parent1, parent2):
        offspring = ['' for allele in range(len(parent1))]
        index_low, index_high = self.__computeLowHighIndexes(parent1)
        offspring[index_low:index_high+1] = list(parent1)[index_low:index_high+1]
        offspring_available_index = list(range(0, index_low)) + list(range(index_high+1, len(parent1)))
        for allele in parent2:
            if '' not in offspring:
                break
            if allele not in offspring:
                offspring[offspring_available_index.pop(0)] = allele
        return ''.join(v for v in offspring)


    def __mutate(self, genome):
        if np.random.random() < self.mutationRate:
            index_low, index_high = self.__computeLowHighIndexes(genome)
            return self.__swap(index_low, index_high, genome)
        else:
            return genome


    def __computeLowHighIndexes(self, string):
        index_low = np.random.randint(0, len(string)-1)
        index_high = np.random.randint(index_low+1, len(string))
        while index_high - index_low > math.ceil(len(string)//2):
            try:
                index_low = np.random.randint(0, len(string))
                index_high = np.random.randint(index_low+1, len(string))
            except ValueError:
                pass
        return (index_low, index_high)


    def __swap(self, index_low, index_high, string):
        string = list(string)
        string[index_low], string[index_high] = string[index_high], string[index_low]
        return ''.join(string)


    def __converged(self, population):
        return all(genome == population[0] for genome in population)

if __name__ == '__main__':
    graph = Graph(10,False)
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


    ga_tsp = GeneticAlgorithmTSP(generations=20, population_size=7, tournamentSize=2, mutationRate=0.2, fit_selection_rate=0.1)

    fittest_path, path_cost = ga_tsp.findFittestPath(graph)
    print ('\nPath: {0}, Cost: {1}'.format(fittest_path, path_cost))
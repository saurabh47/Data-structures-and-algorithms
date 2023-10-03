import math
import random

class Graph:
  def __init__(self, size, directed):
    self.nodes_len = size
    self.roots = {}
    self.nodes = {}
    self.start_city = None
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
  def getPathCost(self, path, will_return=False):
    cost = 0
    for i in range(len(path)-1):
        cost += self.distance(path[i], path[i+1])
    if will_return:
       cost+= self.distance(path[0], path[-1])
    return cost

  def showGraph(self):
    for key, values in self.roots.items():
      print("City {}".format(key))
      for i in range(len(values)):
        print("connected to City {} at distance of {} units".format(values[i][0],values[i][1]))

class GeneticAlgorithmTSP:

    def __init__(self, generations=20, population_size=10, tournamentSize=4, mutationRate=0.1, fit_selection_rate=0.1):
        # the number of routes in each generation
        self.population_size = population_size
        # the number of generations to run the algorithm for
        self.generations = generations
        # the number of routes to select for crossover
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

    def find_fittest_path(self, graph):
        population = self.randomizeCities(graph.vertices())
        # the number of fittest routes to carry over to the next generation
        number_of_fits_to_carryover = math.ceil(self.population_size * self.fit_selection_rate)

        if (number_of_fits_to_carryover > self.population_size):
            raise ValueError('fitness Rate must be in [0,1].')

        print ('Optimizing TSP Route for Graph:\n{0}'.format(graph))

        for generation in range(self.generations):
            print ('\nGeneration: {0}'.format(generation + 1))
            # print ('Population: {0}'.format(population))

            newPopulation = []
            fitness = self.computeFitness(graph, population)
            # print ('Fitness: {0}'.format(fitness))
            fitIndex = self.minCostIndex(fitness)
            print ('Fittest Route: {0} fitness(minium cost): ({1})'.format(population[fitIndex], fitness[fitIndex]))

            if number_of_fits_to_carryover:
                sorted_population = [x for _,x in sorted(zip(fitness,population))]
                fitness = sorted(fitness)
                [newPopulation.append(sorted_population[i]) for i in range( number_of_fits_to_carryover)]
                # print('sorted population: {0}, fitness:{1}\n newPpopulation={2}'.format(sorted_population, fitness, newPopulation))

            # create the remaining population
            # through crossover and mutation
            for gen in range(self.population_size-number_of_fits_to_carryover):
                parent1 = self.tournamentSelection(graph, population)
                parent2 = self.tournamentSelection(graph, population)
                # print("parent1: {0}, parent2: {1}".format(parent1, parent2))
                offspring = self.crossover(parent1, parent2)
                newPopulation.append(offspring)
                # print ('Offspring: {0}\n'.format(offspring))
            # This is the mutation step
            for gen in range(self.population_size-number_of_fits_to_carryover):
                newPopulation[gen] = self.mutate(newPopulation[gen])

            population = newPopulation

            if self.converged(population):
                print("converged", population);
                print ('\nConverged to a local minima.', end='')
                break

        return (population[fitIndex], fitness[fitIndex])

    def randomizeCities(self, graph_nodes):
       result= []
       # nodes without the start city
       nodes = [node for node in graph_nodes if node != graph.start_city]
       for i in range(self.population_size):
          random.shuffle(nodes)
          # add A as the first and last city
          cities = graph.start_city + ''.join(nodes) + graph.start_city
          result.append(cities)
       return result

    # Fitness is the cost of the path
    # lower the cost, higher the fitness
    def computeFitness(self, graph, population):
        fitness = []
        for path in population:
            fitness.append(graph.getPathCost(path))
        return fitness

    # Chooses a parent with the best fitness from a random subset of the population
    # The subset is of size tournamentSize
    # e.g if tournamentSize = 4, then 4 random paths are chosen from the population
    # and the path with the lowest cost is chosen as the parent
    def tournamentSelection(self, graph, population):
        tournament_contestants = random.choices(population, k=self.tournamentSize)
        tournament_contestants_fitness = self.computeFitness(graph, tournament_contestants)
        return tournament_contestants[tournament_contestants_fitness.index(min(tournament_contestants_fitness))]

    # This method uses Partially mapped crossover (PMX) using two points to generate a new offspring
    # from two parents
    def crossover(self,parent1, parent2):
      offspring_length = len(parent1)-2 #excluding first and last city
      offspring = ['' for _ in range(offspring_length)]
      index_low, index_high = self.computeTwoPointIndexes(parent1)
      # Copy the genes from parent1 to the offspring
      offspring[index_low:index_high+1] = list(parent1)[index_low:index_high+1]
      # The remaining genes are copied from parent2
      empty_place_indexes = [i for i in range(offspring_length) if offspring[i] == '']
      for j in parent2[1:-1]:  # Exclude the start and end cities
          if '' not in offspring or not empty_place_indexes:
              break
          if j not in offspring:
              offspring[empty_place_indexes.pop(0)] = j

      offspring = ['A'] + offspring + ['A']
      return ''.join(offspring)


    def mutate(self, genome):
        if random.random() < self.mutationRate:
            index_low, index_high = self.computeTwoPointIndexes(genome)
            return self.swap(index_low, index_high, genome)
        else:
            return genome

    # selects indexes from parents such that the difference between the two indexes is less than half the length of the parent
    #  A B C D E F G H I J A
    #  0 1 2 3 4 5 6 7 8 9 10
    # index_low should be between 1 and 8
    # index_high should be between 2 and 9
    # because the start and end cities are fixed
    def computeTwoPointIndexes(self,parent):
      index_low = random.randint(1, len(parent)-3)
      index_high = random.randint(index_low+1, len(parent)-2)
      # make sure the difference between the two indexes is less than half the length of the parent
      if(index_high - index_low > math.ceil(len(parent)//2)):
          return self.computeTwoPointIndexes(parent)
      else:
          return index_low, index_high

    def swap(self, index_low, index_high, string):
        string = list(string)
        string[index_low], string[index_high] = string[index_high], string[index_low]
        return ''.join(string)

    # check if all the genomes in the population are the same
    # if so, then we have converged to a local minima
    def converged(self, population):
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
    graph.start_city = 'A';

    ga_tsp = GeneticAlgorithmTSP(generations=20, population_size=100, tournamentSize=5, mutationRate=0.1, fit_selection_rate=0.5)

    fittest_path, path_cost = ga_tsp.find_fittest_path(graph)
    print ('\nPath: {0}, Cost: {1}'.format(fittest_path, path_cost))


### output

# Steps in How a Genetic Algorithm Works

# 1. Create an initial population of n chromosomes (suitable solutions for the problem at hand) randomly.
# e.g ['AHBEJIDCFGA', 'AHCEIBFDJGA', 'ACJBGDEFHIA', 'AIJEBGDFHCA', 'ACJEGBDFIHA', 'AGHBFCEIDJA', 'AIDBEHCGFJA']

# 2. Evaluate the fitness of each chromosome in the population.
# e.g [4702.37, 5476.99, 3804.3300000000004, 4524.54, 4757.219999999999, 4939.549999999999, 3974.16]

# 3. Select the best-fit individuals for reproduction. (Parents)
# e.g ['ACJBGDEFHIA', 'AIDBEHCGFJA', 'AIJEBGDFHCA', 'AHBEJIDCFGA', 'ACJEGBDFIHA', 'AGHBFCEIDJA', 'AIDBEHCGFJA']
# In this case, the best-fit individuals are the ones with the lowest cost
# The number of parents selected is based on the fit_selection_rate
# e.g if fit_selection_rate = 0.5, then 50% of the population is selected as parents
# The parents are selected using tournament selection
# Let's say the tournament size is 5, then 5 random individuals are selected from the population
# The best-fit individual from the 5 is selected as a parent
# This process is repeated until the number of parents selected is equal to the fit_selection_rate * population_size


# mahesh@Maheshs-MacBook-Air-M1 algorithms % python3 genetic.py
# Optimizing TSP Route for Graph:
# <__main__.Graph object at 0x104563f10>

# Generation: 1
# Fittest Route: AJBEIDGFHCA fitness(minium cost): (3476.3600000000006)

# Generation: 2
# Fittest Route: ADHEFGJICBA fitness(minium cost): (3277.56)

# Generation: 3
# Fittest Route: AJEDGFHCIBA fitness(minium cost): (3151.24)

# Generation: 4
# Fittest Route: AJBEDFGHICA fitness(minium cost): (3013.32)

# Generation: 5
# Fittest Route: ADHEFGICJBA fitness(minium cost): (2864.2299999999996)

# Generation: 6
# Fittest Route: ABDHEFGICJA fitness(minium cost): (2797.5499999999997)

# Generation: 7
# Fittest Route: ABDHEFGICJA fitness(minium cost): (2797.5499999999997)

# Generation: 8
# Fittest Route: ABDHEFGICJA fitness(minium cost): (2797.5499999999997)

# Generation: 9
# Fittest Route: ABEFGHDCIJA fitness(minium cost): (2776.9999999999995)

# Generation: 10
# Fittest Route: ABDEHFGICJA fitness(minium cost): (2761.7299999999996)

# Generation: 11
# Fittest Route: ABDEHFGICJA fitness(minium cost): (2761.7299999999996)

# Generation: 12
# Fittest Route: ABDEFGHICJA fitness(minium cost): (2627.4799999999996)

# Generation: 13
# Fittest Route: ABDEFGHICJA fitness(minium cost): (2627.4799999999996)

# Generation: 14
# Fittest Route: ABDEFGHICJA fitness(minium cost): (2627.4799999999996)

# Generation: 15
# Fittest Route: ABDEFGHICJA fitness(minium cost): (2627.4799999999996)

# Generation: 16
# Fittest Route: ABDEFGHICJA fitness(minium cost): (2627.4799999999996)

# Generation: 17
# Fittest Route: ABDEFGHICJA fitness(minium cost): (2627.4799999999996)

# Generation: 18
# Fittest Route: ABDEFGHICJA fitness(minium cost): (2627.4799999999996)

# Generation: 19
# Fittest Route: ABDEFGHICJA fitness(minium cost): (2627.4799999999996)

# Generation: 20
# Fittest Route: ABDEFGHICJA fitness(minium cost): (2627.4799999999996)

# Path: ABDIFGHECJA, Cost: 2627.4799999999996
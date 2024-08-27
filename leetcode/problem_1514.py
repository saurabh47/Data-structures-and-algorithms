### Problem 1514. Path with maximum Probability
### tags: Graph, Dijkstra, Heap

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = {}
        def addEdge(a, b, prob):
            if a not in adj_list:
                adj_list[a] = []
            if b not in adj_list:
                adj_list[b] = []
            adj_list[a].append([b, prob])
            adj_list[b].append([a, prob])

        for i in range(len(edges)):
            prob = succProb[i]
            edge = edges[i]
            addEdge(edge[0], edge[1], prob)

        max_heap = [(-1, start_node)]
        visited = set()
        while(max_heap):
            prob, currNode = heapq.heappop(max_heap)
            visited.add(currNode)
            if(currNode == end_node):
                return prob * -1
            if(currNode not in adj_list):
                break
            for neighbor, n_prob in adj_list[currNode]:
                if(neighbor not in visited):
                    heapq.heappush(max_heap, (prob * n_prob, neighbor))
        return 0
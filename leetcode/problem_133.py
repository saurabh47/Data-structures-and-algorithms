### Problem 133. Clone Graph (Medium): https://leetcode.com/problems/clone-graph/

### tags: Graph, BFS, DFS Hash Table
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
# BFS Solution
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = deque()
        if(node is None):
            return node
        q.append(node)
        node_map = {}
        node_map[node.val] = Node(node.val, [])
        while(len(q) != 0):
            top = q.popleft()
            for n in top.neighbors:
                if(n.val not in node_map):
                    q.append(n)
                    node_map[n.val] = Node(n.val,[])
                node_map[top.val].neighbors.append(node_map[n.val])
        return node_map[node.val]

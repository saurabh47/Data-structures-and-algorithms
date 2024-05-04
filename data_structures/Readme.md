### Data Structures

- Linked Lists
- Binary Trees
- Binary Search Trees
- Graphs

#### Trees

- [Binary Tree]()
A Binary Tree Data Structure is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. It is commonly used in computer science for efficient storage and retrieval of data, with various operations such as insertion, deletion, and traversal.


*Note: Docs generated via Github copilot*
#### Linked Lists

- [Singly Linked List](singly_linked_list.md)

    Linked lists are a data structure that are linear data structures made up of nodes. Each node contains a value and a pointer to the next node. The first node in the linked list is called the head node. The last node in the linked list is called the tail node.

    Linked lists are very efficient for searching and traversing.

    The time complexity for searching and traversing a linked list is O(n) where n is the number of nodes in the linked list. While, The time complexity for inserting and deleting a node in a linked list is O(1) as compared to O(n) in an array. This is because, in an array, we have to shift the elements to the right or left when we insert or delete an element.But in linked list it is assumed that we have a pointer to the location where we want to insert an element. So, we just have to change the pointer of the previous node to point to the new node and the pointer of the new node to point to the next node. This is why linked lists are very efficient for inserting and deleting elements.

- [Doubly Linked List](doubly_linked_list.md)

    In Doubley Linked List, we have two pointers, one pointing to the next node and the other pointing to the previous node.
    In Singly Linked List, we have only one pointer, pointing to the next node.
    The advantage of using Doubley Linked List is that we can traverse the list in both the directions, i.e. forward and backward. This is not possible in Singly Linked List.
    The disadvantage of using Doubley Linked List is that it takes more memory as compared to Singly Linked List.

#### Binary Trees

    A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right.

    Binary Tree traversal is the process of visiting each node in a tree exactly once. There are three types of traversal: preorder, inorder, and postorder.

    Binary Tree Traversal is a very important topic in Data Structures. It is used in many other algorithms like Binary Search Tree, Heap, Graph, etc. It is also used in many other applications like in parsing, expression evaluation, etc.

### Graphs

    A graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph can be defined as, A Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes.

    Graphs are used to solve many real-life problems. Graphs are used to represent networks. The networks may include paths in a city or telephone network or circuit network. Graphs are also used in social networks like linkedIn, Facebook. For example, in Facebook, each person is represented with a vertex(or node). Each node is a structure and contains information like person id, name etc. To represent friends relationship, edges are used.

    - Adjacency Matrix
        Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. Adjacency matrix for undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.
            Adjacency matrix have following drawbacks:
            1. Consumes more space O(V^2). Even if the graph is sparse(contains less number of edges), it consumes the same space.
            2. Takes O(V^2) time to iterate over all the edges of the graph.
            3. Queries like whether there is an edge from vertex 'u' to vertex 'v' are not efficient and can be done O(1).

    - Adjacency List
        An array of lists is used. Size of the array is equal to the number of vertices. Let the array be array[]. An entry array[i] represents the list of vertices adjacent to the ith vertex. This representation can also be used to represent a weighted graph. The weights of edges can be represented as lists of pairs. Following is adjacency list representation of the above graph.
            Adjacency list is better than adjacency matrix when it comes to storage. If there are fewer edges, it saves space. In the worst case, there can be C(V, 2) number of edges in a graph thus consuming O(V^2) space. Adding a vertex is easier.
            Queries like whether there is an edge from vertex u to vertex v are efficient and can be done O(LogV).
            It doesn’t occupy extra space like adjacency matrix.
            In the worst case, there can be C(V, 2) number of edges in a graph thus consuming O(V^2) space. Adding a vertex is easier.

    - Breadth First Search
        Breadth First Search is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node). You must then move towards the next-level neighbour nodes.

        e.g

        ```
               1 ----- 3 -- -- 0
             / |     / |     / |
           /   |    /  |    /  |
         5     |   /   |   /   |
           \   |  /    |  /    |
             \ | /     | /     |
               2 ----- 4 -- -- 6

        ```
        The output of BFS traversal from a node 2 is: 2, 5, 3, 1, 4, 0, 6. If you observe carefully, you will notice that the nodes are visited level wise. First, all the nodes of the first level are visited, then nodes of second level, and so on. The algorithm for BFS traversal is as follows:
        The output of BFS traversal from a node 0 is: 0, 3, 4, 6, 2, 1, 5
        The output of BFS traversal from a node 5 is: 5, 1, 2, 3, 4, 0, 6


### Problems to solve

- Height and Depth of a node in a Binary Tree
Given a Binary Tree consisting of N nodes and a integer K, the task is to find the depth and height of the node with value K in the Binary Tree. 

The depth of a node is the number of edges present in path from the root node of a tree to that node.
The height of a node is the number of edges present in the longest path connecting that node to a leaf node.


- Given a Binary tree and a node. The task is to search and check if the given node exists in the binary tree or not. If it exists, print YES otherwise print NO.


- Given a tree and a node, the task is to find the parent of the given node in the tree. Print -1 if the given node is the root node.

- Given a Binary tree and a node. The task is to search and check if the given node exists in the binary tree or not. If it exists, print YES otherwise print NO.



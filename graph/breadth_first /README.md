# BFS in Graphs

The act of searching or traversing through a graph data structure is fairly simple: it just means that we’re probably visiting every single vertex (and by proxy, every single edge) in the graph. At it’s very core, the only difference between traversing a graph by breadth or by depth is the order in which we visit the vertices in a graph. In other words, the order in which the vertices of a graph are visited is actually how we can classify different graph traversal algorithms.

## Challenge

- Step-by-step BFS traversal
    - 1 - Add a node/vertex from the graph to a queue of nodes to be “visited”.
    - 2 - Visit the topmost node in the queue, and mark it as such.
    - 3 - If that node has any neighbors, check to see if they have been “visited” or not.
    - 4 - Add any neighboring nodes that still need to be “visited” to the queue.
    - 5 - Remove the node we’ve visited from the queue.

## Approach & Efficiency

Worst case scenario for BFS traversal:

- Time compexity: O(V+E)
- Space Complexity: O(n)
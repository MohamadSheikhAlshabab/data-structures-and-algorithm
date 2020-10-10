def bfs_traverse(graph, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)   
            for nextNode in graph[node]:
                if nextNode not in visited:
                    queue.append(nextNode)
    return visited

graph = {'A': set(['B', 'C', 'F']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['A', 'C', 'E'])}
print(bfs_traverse(graph, 'A'))

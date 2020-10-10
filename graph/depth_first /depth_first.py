def dfs(graph, source, path=[]):
    if source not in path:
        path.append(source)
        if source not in graph:
            return path
        for neighbor in graph[source]:
            path = dfs(graph, neighbor, path)
    return path

if __name__ == "__main__":
    graph = {"A": ["B", "D"],
                "B": ["A",'D','C'],
                "C": ["B", "G"],
                "D": ["A",'F','H','E','B'],
                "E": ["D"],
                "F": ["D",'H'],
                "H": ['D','F'],
                }

    path = graph_dfs(graph, "A")
    print(path)
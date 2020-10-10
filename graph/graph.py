class Node:
    def __init__(self, value):
        self.value = value
class Graph:
    def __init__(self):
        """
        This is initial method of the graph
        """
        try:
            self._adjacency_list = {}
        except Exception as err:
            print(f"There is an error in init as {err}")

    def add_node(self, value):
        """
        This method to add node to graph
        """
        try:
            node = Node(value)
            if value in self._adjacency_list:
                print('Vertex',value,' already exists')
            self._adjacency_list[node.value] = []
        except Exception as err:
            print(f"There is error in add_node as {err}")

    def add_edge(self, start_node, end_node, weight=1):
        """
        This method to add edge to graph
        """
        try:
            if start_node not in self._adjacency_list.keys():
                print("Vertex ", start_node, " does not exist.")
            elif end_node not in self._adjacency_list.keys():
                print("Vertex ", end_node, " does not exist.")
            else:
                temp = [end_node, weight]
                self._adjacency_list[start_node].append(temp)
        except Exception as err:
            print(f"There is error in add_edge as {err}")

    def get_nodes(self):
        """
        This method to return nodes
        """
        try:
            for vertex in self._adjacency_list:
                for edges in self._adjacency_list[vertex]:
                    print(vertex, " -> ", edges[0], " edge weight: ", edges[1])
        except Exception as err:
            print(f"There is error in get_nodes as {err}")

    def get_neighbors(self, node):
        """
        This method to return neighbors
        """
        try:
            for edges in self._adjacency_list[node]:
                print(node, " -> ", edges[0], " edge weight: ", edges[1])
        except Exception as err:
            print(f"There is an error in get_neighbors as {err}")

    def size(self):
        """
        This method to return size of graph
        """
        try:
            return len(self._adjacency_list)
        except Exception as err:
            print(f"There is an error in size as {err}")

    def bfs(self,graph, start):
        visited, queue = set(), [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for nextNode in graph[node]:
                    if nextNode not in visited:
                        queue.append(nextNode)
        return visited

if __name__ == "__main__":
    g = Graph()
    graph = {'A': set(['B', 'C', 'F']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['A', 'C', 'E'])}
    print(g._adjacency_list)
    g.add_node('10')
    g.add_node('5')
    g.add_node('9')
    g.add_node('44')
    g.add_edge('10', '5', 3)
    g.add_edge('10', '10', 6)
    g.add_edge('5', '44', 2)
    g.add_edge('44', '9', 4)
    g.add_edge('44', '10', 1)
    g.add_edge('5', '10', 7)
    g.add_edge('9', '10', 8)
    g.get_neighbors('5')
    print(g.size())
    print(g.bfs(graph,'A'))
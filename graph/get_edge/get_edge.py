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
                return self._adjacency_list[node]
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
    
def list_to_dict(cities):
    output = {}
    for city in cities:
        output[city[0]] = city[1]
    return output

def get_trip(graph, cities):
    cost = 0
    for city in range(len(cities)-1):
        direct_path = list_to_dict(graph.get_neighbors(cities[city]))
        if cities[city+1] not in direct_path:
            return 'False, $0'
        cost += direct_path[cities[city+1]]
    return f'True, ${cost}'


if __name__ == "__main__":
    g2 = Graph()
    g2.add_node("Pandora")
    g2.add_node("Metroville")
    g2.add_node("Arendelle")
    g2.add_node("Monstropolis")
    g2.add_node("Narnia")
    g2.add_node("Naboo")
    g2.add_edge('Pandora', 'Arendelle', 150)
    g2.add_edge('Pandora', 'Metroville', 82)
    g2.add_edge('Arendelle', 'Metroville', 99)
    g2.add_edge('Arendelle', 'Monstropolis', 42)
    g2.add_edge('Metroville', 'Monstropolis', 105)
    g2.add_edge('Metroville', 'Narnia', 37)
    g2.add_edge('Metroville', 'Naboo', 26)
    g2.add_edge('Naboo', 'Narnia', 250)
    g2.add_edge('Naboo', 'Monstropolis', 73)
    print( get_trip(g2, ['Metroville','Monstropolis']))
    print( get_trip(g2,['Naboo', 'Pandora']))
    print( get_trip(g2,['Naboo', 'Arendelle','Pandora'])) 
from graph.graph import Graph , Node

def test_graph_size():
    g = Graph()
    # print(g._adjacency_list)
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
    # g.get_neighbors('5')
    actual = print(g.size())
    expected = 4
    assert actual == expected

def test_graph_adjacency_list():
    g = Graph()
    
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
    # g.get_neighbors('5')
    actual = print(g._adjacency_list)
    expected = {'10': [['5', 3], ['10', 6]], '5': [['44', 2], ['10', 7]], '9': [['10', 8]], '44': [['9', 4], ['10', 1]]}
    assert actual == expected

# def test_graph():
#     g = Graph()
#     print(g._adjacency_list)

#     actual = 
#     expected = 

#     assert actual == expected

# def test_graph():
#     g = Graph()
#     print(g._adjacency_list)

#     actual = 
#     expected = 

#     assert actual == expected
from graph.graph import Graph , Node
import pytest

def test_graph_size():
    g = Graph()

    g.add_node('10')
    g.add_node('5')
    g.add_node('9')
    g.add_node('44')

    actual = g.size()
    expected = 4
    assert actual == expected

def test_graph_adjacency_list():
    g = Graph()
    
    g.add_node('10')
    g.add_node('5')
    g.add_node('9')
    g.add_node('44')

    actual = list(g._adjacency_list)
    expected = ['10', '5', '9', '44']

    assert actual == expected

def test_breadth_first_not_in_graph():
    g = Graph()
    graph = {'A': set(['99', '90', '100']),}

    g.add_node('99')
    g.add_node('90')
    g.add_node('100')

    with pytest.raises(KeyError):
        g.bfs(graph,'101')  

def test_breadth_first_start_from_end():
    g = Graph()
    graph = {'A': set(['B', 'C', 'F']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['A', 'C', 'E'])}

    assert g.bfs(graph,'A') == {'E', 'A', 'D', 'B', 'F', 'C'}

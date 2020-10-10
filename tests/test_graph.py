from graph.graph import Graph , Node
import pytest

@pytest.fixture
def g2():
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

    return g2

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

def test_trip_1(g2):
    graph = g2
    assert g2.get_trip(graph, ['Metroville', 'Narnia']) == 'True, $37'


def test_trip_2(g2):
    graph = g2
    assert g2.get_trip(graph, ['Metroville', 'Monstropolis', ]) == 'True, $105'

def test_no_direct_path1(g2):
    graph = g2
    assert g2.get_trip(graph, ['Naboo', 'Pandora']) == 'False, $0'

def test_no_direct_path2(g2):
    graph = g2
    assert g2.get_trip(graph, ['Naboo', 'Arendelle','Pandora']) == 'False, $0'


def test_city_not_in_graph(g2):
    graph = g2
    assert g2.get_trip(graph, ['Metroville', 'Pandora']) == 'False, $0'


def test_returning_the_correct_path():
    g=Graph()
    graph2 = {"A": ["B", "C",'G','D',"E",'H',"F"],
            "B": ['C','G'],
            "C": ["G"],
            "D": ['E','H','F'],
            "E": ["D"],
            "F": ['H'],
            "H": ["D"],
            "G":["C"],
            }
    path = g.dfs(graph2, "A")
    output=",".join(path)
    print(output)
    actual = path
    expected = ['A','B','C','G','D','E','H','F']
    assert actual == expected

def test_pasing_empty_graph():
    g=Graph()
    g2={}
    actual = g.dfs(g2,'A',path=[])
    expected = ['A']
    assert expected == actual
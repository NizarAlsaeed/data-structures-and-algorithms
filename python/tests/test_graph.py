import pytest
from Data_Structures.graph.graph import Graph

def test_add_node(graph_instance):
    """Node can be successfully added to the graph"""
    graph_instance[0].add_node(5)
    actual = graph_instance[0].get_nodes()
    expected = [1,2,3,5]
    assert actual == expected

def test_add_edge(graph_instance):
    """An edge can be successfully added to the graph"""
    graph_instance[0].add_edge(graph_instance[2],graph_instance[3])
    actual = graph_instance[0].get_neighbors(graph_instance[3])
    expected = [(2,1)]
    assert actual == expected

def test_get_nodes():
    """A graph with only one node and edge can be properly returned
    An empty graph properly returns null"""
    graph = Graph()
    actual = graph.get_nodes()
    expected = []
    assert actual == expected
    node = graph.add_node('only me')
    graph.add_edge(node,node)
    actual = graph.get_neighbors(node)
    print(actual)
    expected = [('only me',1)]
    assert actual == expected

def test_get_neighbors(graph_instance):
    """All appropriate neighbors can be retrieved from the graph
    Neighbors are returned with the weight between nodes included"""
    actual = graph_instance[0].get_neighbors(graph_instance[1])
    expected = [(2,10)]
    assert actual == expected

def test_size(graph_instance):
    """The proper size is returned, representing the number of nodes in the graph"""
    actual = graph_instance[0].size()
    expected = 3
    assert actual == expected


@pytest.fixture
def graph_instance():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    graph.add_edge(node1, node2, 10)
    return graph,node1,node2,node3
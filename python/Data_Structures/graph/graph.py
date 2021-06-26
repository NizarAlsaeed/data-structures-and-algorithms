
class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, starting_node, ending_node, weight=1):
        self.starting_node = starting_node
        self.ending_node = ending_node

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """ Arguments: value
            Returns: The added node
            Add a node to the graph """
        if value not in [key.value for key in self._adjacency_list.keys()]:
            new_node = Vertex(value)
            self._adjacency_list.setdefault(new_node,[])
            return new_node
        else:
            raise ValueError("Node already exists in the graph")

    def add_edge(self, starting_node, ending_node, weight=1):
        """ Arguments: 2 nodes to be connected by the edge, weight (optional)
            Returns: nothing
            Adds a new edge between two nodes in the graph
            If specified, assign a weight to the edge
            Both nodes should already be in the Graph """
        if starting_node in self._adjacency_list.keys() and ending_node in self._adjacency_list.keys():
            new_edge = Edge(starting_node, ending_node, weight=weight)
            self._adjacency_list.get(starting_node).append((new_edge.ending_node.value,weight))
            if starting_node != ending_node:
                self._adjacency_list.get(ending_node).append((new_edge.starting_node.value,weight))
        else:
            raise ValueError('One of the Nodes does not exist in the graph')

    def get_nodes(self):
        """ Arguments: none
            Returns all of the nodes in the graph as a collection (set, list, or similar) """
        return [key.value for key in self._adjacency_list.keys()]

    def get_neighbors(self, node):
        """ Arguments: node
            Returns a collection of edges connected to the given node
            Include the weight of the connection in the returned collection """
        if node in self._adjacency_list.keys():
            return self._adjacency_list.get(node)
        else:
            raise ValueError('Node does not exist in the graph')

    def size(self):
        """ Arguments: none
            Returns the total number of nodes in the graph"""
        return len(self._adjacency_list.keys())

if __name__ == '__main__':
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    graph.add_edge(node1, node2, 10)
    print(graph.get_nodes())
    print(graph.get_neighbors(node2))
    print(graph.size())

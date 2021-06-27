from collections import  deque
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
            self._adjacency_list.get(starting_node).append((new_edge.ending_node,weight))
            if starting_node != ending_node:
                self._adjacency_list.get(ending_node).append((new_edge.starting_node,weight))
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

    def breadth_first(self, starting_node, action=print):
        """ Arguments: Node
            Return: A collection of nodes in the order they were visited.
            Display the collection """
        frontier = deque()
        explored = set()
        root = starting_node
        frontier.append(root)
        action(root.value)
        while frontier:
            current = frontier.popleft()
            explored.add(current)
            neighbors = self.get_neighbors(current)

            for node in neighbors:
                if (node[0] not in explored) and (node[0] not in frontier) :
                    action(node[0].value)
                    frontier.append(node[0])

if __name__ == '__main__':
    graph = Graph()
    node1 = graph.add_node("pandora")
    node2 = graph.add_node("Arendelle")
    graph.add_edge(node1, node2)
    node3 = graph.add_node("Metroville")
    node4 = graph.add_node("Monstropolis")
    graph.add_edge(node2, node3)
    graph.add_edge(node2, node4)
    graph.add_edge(node3, node4)
    node5 = graph.add_node("Narnia")
    node6 = graph.add_node("Naboo")
    graph.add_edge(node3, node5)
    graph.add_edge(node3, node6)
    graph.add_edge(node4, node6)
    graph.add_edge(node5, node6)
    # print(graph.get_nodes())
    # print(graph.get_neighbors(node4))
    # print(graph.size())
    print(graph.breadth_first(node1))

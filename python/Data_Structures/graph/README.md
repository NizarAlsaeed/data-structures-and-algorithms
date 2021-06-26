# Graphs
<!-- Short summary or background information -->
A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph.
## Challenge
<!-- Description of the challenge -->
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add node

- add edge

- get nodes

- get neighbors

- size


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Implemented graph using adjacency list representation
## API
<!-- Description of each method publicly available in your Graph -->
```python
graph = Graph()
node1 = graph.add_node(1)
node2 = graph.add_node(2)
node3 = graph.add_node(3)
graph.add_edge(node1, node2, 10)
print(graph.get_nodes())
print(graph.get_neighbors(node3))
print(graph.size())

>> [1, 2, 3]
   [(1, 10)]
   3
```

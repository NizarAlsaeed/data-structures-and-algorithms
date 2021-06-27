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

- breadth first

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Implemented graph using adjacency list representation
## API
<!-- Description of each method publicly available in your Graph -->
```python
# breadth first search
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

>>pandora
  Arendelle
  Metroville
  Monstropolis
  Narnia
  Naboo
```

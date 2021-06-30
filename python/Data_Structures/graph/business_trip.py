"""
Given a business trip itinerary, and an Alaska Airlines route map, is the trip
possible with direct flights? If so, how much will the total trip cost be?
"""
from graph import Graph

def business_trip(graph:Graph, trip:list)->tuple:
    """ Arguments: graph, array of city names
        Return: cost or null
        Determine whether the trip is possible with direct flights, and how much it would cost."""

    # possible with direct flights?
    # ans: if node is neighbor of next node in the trip
    # how much it would cost?
    # ans: sum of edges weights
    cost = 0
    for i in range(len(trip)-1):
         city = trip[i]
         next_city = trip[i+1]
         city_neighbors = graph.get_neighbors(city)
         next_neighbor_info = [c for c in city_neighbors if next_city == c[0]]
         if not len(next_neighbor_info):
            return (False,0)
         cost += next_neighbor_info[0][1]

    return (True, cost)

if __name__ == '__main__':
    graph = Graph()
    node1 = graph.add_node("pandora")
    node2 = graph.add_node("Arendelle")
    graph.add_edge(node1, node2,150)
    node3 = graph.add_node("Metroville")
    node4 = graph.add_node("Monstropolis")
    graph.add_edge(node1, node3,82)
    graph.add_edge(node2, node3,99)
    graph.add_edge(node2, node4,42)
    graph.add_edge(node3, node4,105)
    node5 = graph.add_node("Narnia")
    node6 = graph.add_node("Naboo")
    graph.add_edge(node3, node5,37)
    graph.add_edge(node3, node6,26)
    graph.add_edge(node4, node6,73)
    graph.add_edge(node5, node6,250)

    print(business_trip(graph, [node5, node2, node6]))
    # ["Metroville", "Pandora", ] 	True, $82
    # ["Arendelle", "New Monstropolis", "Naboo"] 	True, $115
    # ["Naboo", "Pandora"] 	False, $0
    # ["Narnia", "Arendelle", "Naboo"] 	False, $0

import weighted_graph

g = weighted_graph.Graph()
g.add_edge("A", "B", 2)
g.add_edge("A", "C", 2)
g.add_edge("A", "E", 0)
g.add_edge("B", "D", 0)
g.add_edge("B", "F", 0)
g.add_edge("C", "G", 2)
g.add_edge("G", "B", 1)
g.add_edge("F", "E")
g.add_edge("E", "A", 0)
g.add_node("I")
pathFW = g.FloydWarshall('A', 'I')
pathD = g.dijkstra('A', 'I')

print(pathFW)
print(pathD)

import weighted_graph

g = weighted_graph.Graph()
g.add_edge(1, 2, 2)
g.add_edge(2, 3, 4)
print(g.FloydWarshall(1, 3))

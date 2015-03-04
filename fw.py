import weighted_graph

g = weighted_graph.Graph()
g.add_edge(1, 2, 2)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 5)
g.add_edge(2, 4, 1)
pathFW = g.FloydWarshall(1, 4)
pathD = g.dijkstra(1, 4)

print(pathFW)
print(pathD)

#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
import stack as stk
import queue as que
from collections import OrderedDict as od
import numpy as np


class Graph(object):
    ''' Create an empty graph.
        Nodes must be hashable values.'''
    def __init__(self):
        self.graph = od()

    def nodes(self):
        ''' Return all the nodes in the graph. '''
        return self.graph.keys()

    def edges(self):
        ''' Return all the edges in the graph as a list of tuples. '''
        return [(key, key2, value2)
                for key, value in self.graph.iteritems()
                for key2, value2 in value.iteritems()]

    def add_node(self, node):
        ''' Add a node to the graph.
            We are using dictionaries to store neighbors and weights so we
            don't have to loop through lists to remove neighbros and weights.
            '''
        self.graph.setdefault(node, od())

    def add_edge(self, node1, node2, weight=0):
        ''' Add an edge to the graph. '''
        # Add node1 to graph
        self.graph.setdefault(node1, od())
        # Add edge
        self.graph[node1].update({node2: weight})
        # Check if node1 is in the graph
        if node2 not in self.graph:
            self.add_node(node2)

    def del_edge(self, node1, node2):
        ''' Delete an edge to the graph. '''
        try:
            del self.graph[node1][node2]
        except KeyError:
            raise KeyError('One of the given nodes not in graph'.format(node1))

    def del_node(self, node):
        ''' Delete a node from the graph. '''
        try:
            del self.graph[node]
            # Delete the node from any neighbor lists it is in.
            for value in self.graph.itervalues():
                    try:
                        del value[node]
                    except KeyError:
                        pass
        except KeyError:
            raise KeyError('{} not in graph'.format(node))

    def has_node(self, node):
        ''' Return True or False if the node is in the graph or not. '''
        return node in self.graph

    def neighbors(self, node):
        ''' Return the neighbors of a node. '''
        try:
            return self.graph[node].keys()
        except KeyError:
            raise KeyError('{} not in graph'.format(node))

    def adjacent(self, node1, node2):
        ''' Check is if two nodes have an edge connecting them. '''
        try:
            return node2 in self.graph[node1].keys()
        except KeyError:
            raise KeyError('{} not in graph'.format(node1))

    def weight(self, node1, node2):
        return self.graph[node1][node2]

    def depth_first_traversal(self, node):
        ''' Depth first graph traversal. '''
        # Initialize path
        path = []

        # Initilize stack
        stack = stk.Stack()

        # Push node onto stack.
        stack.push(node)

        while stack.top:
            test_node = stack.pop()
            if test_node not in path:
                path.append(test_node)
                for neighbor in self.neighbors(test_node):
                    stack.push(neighbor)

        return path

    def breadth_first_traversal(self, node):
        ''' Breadth first graph traversal. '''
        path = []

        queue = que.Queue()

        path.append(node)

        queue.enqueue(node)

        while queue.front:
            test_node = queue.dequeue()

            for neighbor in self.neighbors(test_node):
                if neighbor not in path:
                    path.append(neighbor)
                    queue.enqueue(neighbor)
        return path

    def dijkstra(self, start_node, end_node):
        ''' Dijkstra shortest path finder.'''
        # Initialization of previous and distance arrays
        itarget = self.nodes().index(end_node)
        distance = [np.inf] * len(self.nodes())
        distance[self.nodes().index(start_node)] = 0
        previous = [None] * len(self.nodes())
        # Initialize node indicies
        Q = range(len(self.nodes()))

        while len(Q):
            # Truncated distance array based on Q
            tmp = [distance[i] for i in Q]
            iU = Q[tmp.index(min(tmp))]
            if self.nodes()[iU] == end_node:
                return self.build_path_Dijkstra(distance,
                                                previous,
                                                itarget,
                                                start_node)

            Q.remove(iU)

            for V in self.neighbors(self.nodes()[iU]):
                iV = self.nodes().index(V)
                alt = distance[iU] + self.weight(self.nodes()[iU], V)

                if alt < distance[iV]:
                    distance[iV] = alt
                    previous[iV] = iU
        return self.build_path_Dijkstra(distance,
                                        previous,
                                        itarget,
                                        start_node)

    def build_path_Dijkstra(self, distance, previous, itarget, start_node):
        S = []
        while previous[itarget] is not None:
            S = [self.nodes()[itarget]] + S
            itarget = previous[itarget]
        S = [self.nodes()[itarget]] + S

        if (start_node not in S):
            return 'No path from {} to {}'.format(start_node,
                                                  self.nodes()[itarget])
        else:
            return S

    def FloydWarshall(self, start, goal):
        ''' Floyd-Warshall shortest path finder.'''
        # Initiliaze array of minimum distances and set to Inifinity
        dist = np.zeros((len(self.nodes()), len(self.nodes())))
        dist[dist == 0] = np.inf

        # Initiliaze array of node indicies and set to None
        nxt = np.zeros((len(self.nodes()), len(self.nodes())))
        nxt[nxt == 0] = None

        # Initialize diagnol (distance to self) as zero
        np.fill_diagonal(dist, 0)

        # Floyd Warshall - Find Paths
        for edge in self.edges():
            dist[self.nodes().index(edge[0])][self.nodes().index(edge[1])] = edge[2]
            nxt[self.nodes().index(edge[0])][self.nodes().index(edge[1])] = self.nodes().index(edge[1])

        # Build distance array and next node array
        for k in range(len(self.nodes())):
            for i in range(len(self.nodes())):
                for j in range(len(self.nodes())):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        nxt[i][j] = nxt[i][k]

        # Build path of indecies
        iU = self.nodes().index(start)
        if nxt[iU][self.nodes().index(goal)] is None:
            return []
        path_idx = [iU]
        while iU != self.nodes().index(goal):
            try:
                iU = nxt[iU][self.nodes().index(goal)]
                path_idx.append(iU)
            except IndexError:
                raise IndexError('Nodes not connected')

        # Path reconstruction
        return [self.nodes()[int(i)] for i in path_idx]


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2, 0)
    g.add_edge(2, 3, 0)
    path = g.FloydWarshall(1, 3)

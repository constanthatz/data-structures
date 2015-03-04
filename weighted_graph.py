#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
import stack as stk
import queue as que
from Queue import heapq
from collections import OrderedDict as od
import numpy as np


class Graph(object):
    ''' Create an empty graph.
        Nodes must be hashable values.'''
    def __init__(self):
        self.graph = {}

    def nodes(self):
        ''' Return all the nodes in the graph. '''
        return self.graph.keys()

    def edges(self):
        ''' Return all the edges in the graph as a list of tuples. '''
        # for key, value in self.graph.iteritems():
        #     for i, item in enumerate(value['neighbors']):
        #         return (key, item, value['weights'][i])
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
        # print(queue.front.val)

        while queue.front:
            test_node = queue.dequeue()

            for neighbor in self.neighbors(test_node):
                if neighbor not in path:
                    path.append(neighbor)
                    queue.enqueue(neighbor)
        return path

    def dijkstra(self, start_node, end_node):
        # List of nodes
        nodes = self.nodes()

        # Initialization
        iU = nodes.index(start_node)
        itarget = nodes.index(end_node)
        distance = [np.inf]*len(nodes)
        distance[iU] = 0
        previous = [None]*len(nodes)
        Q = []
        for i in range(len(nodes)):
            Q.append(i)

        while len(Q):
            tmp = []
            for i in Q:
                tmp.append(distance[i])
            minIndexQ = tmp.index(min(tmp))
            minIndex = Q[minIndexQ]
            iU = minIndex
            if nodes[iU] == end_node:
                return self.build_path_Dijkstra(distance, previous, itarget)

            Q.remove(iU)

            for V in self.neighbors(nodes[iU]):
                iV = nodes.index(V)
                alt = distance[iU] + self.weight(nodes[iU], V)

                if alt < distance[iV]:
                    distance[iV] = alt
                    previous[iV] = iU
        return self.build_path_Dijkstra(distance, previous, itarget)

    def build_path_Dijkstra(self, distance, previous, itarget):
        nodes = self.nodes()
        S = []
        iT = itarget
        while previous[iT] is not None:
            S = [nodes[iT]] + S
            iT = previous[iT]
        return [nodes[iT]] + S

    def FloydWarshall(self, start, goal):

        # List of nodes
        nodes = self.nodes()

        # Number of nodes
        number_of_nodes = len(self.nodes())

        # Initiliaze array of minimum distances and set to Inifinity
        dist = np.zeros((number_of_nodes, number_of_nodes))
        dist[dist == 0] = np.inf

        # Initiliaze array of node indicies and set to None
        nxt = np.zeros((number_of_nodes, number_of_nodes))
        nxt[nxt == 0] = None

        # List of edges with weights
        edges = self.edges()

        for i in range(number_of_nodes):
            dist[i][i] = 0

        # Floyd Warshall - Find Paths
        # print(edges)
        for edge in edges:
            U = edge[0]
            V = edge[1]
            weight = edge[2]
            iU = nodes.index(U)
            iV = nodes.index(V)
            dist[iU][iV] = weight
            nxt[iU][iV] = iV

        for k in range(number_of_nodes):
            for i in range(number_of_nodes):
                for j in range(number_of_nodes):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        nxt[i][j] = nxt[i][k]

        # print(dist)
        # print(nxt)
        # Path reconstruction
        U = start
        V = goal
        iU = self.nodes().index(U)
        iV = self.nodes().index(V)
        if nxt[iU][iV] is None:
            return []
        path_idx = [iU]
        while iU != iV:
            # print(U)
            iU = nxt[iU][iV]
            path_idx.append(iU)

        S = []
        for i in path_idx:
            S.append(nodes[int(i)])

        return S


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2, 0)
    g.add_edge(2, 3, 0)
    path = g.FloydWarshall(1, 3)

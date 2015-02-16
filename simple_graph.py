#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Graph(object):
    ''' Create an empty graph. '''
    def __init__(self):
        self.graph = {}

    def nodes(self):
        ''' Return all the nodes in the graph. '''
        return self.graph.keys()

    def edges(self):
        ''' Return all teh edges in the graph as a list of tuples. '''
        return [(key, item) for key, value in self.graph.iteritems()
                for item in value]

    def add_node(self, node):
        ''' Add a node to the graph. '''
        self.graph.setdefault(node, [])

    def add_edge(self, node1, node2):
        ''' Add an edge to the graph. '''
        try:
            # Check if node1 is in the graph and add edge
            self.graph[node1].append(node2)
            # Check if node1 is in the graph
            if node2 not in self.graph:
                self.add_node(node2)
        except KeyError:
            # Add node1 to graph
            self.add_node(node1)
            # Add edge
            self.graph[node1].append(node2)
            # Check if node1 is in the graph
            if node2 not in self.graph:
                self.add_node(node2)

    def del_node(self, node):
        ''' Delete a node from the graph. '''
        try:
            del self.graph[node]
            # Delete the node from any neighbor lists it is in.
            for value in self.graph.itervalues():
                if node in value:
                    value.remove(node)
        except KeyError:
            raise KeyError('node not in graph')

    def has_node(self, node):
        ''' Return True or False ifthe node is in the graph or not. '''
        return node in self.graph

    def neighbors(self, node):
        ''' Return the neighbors of a node. '''
        try:
            return self.graph[node]
        except KeyError:
            raise KeyError('node not in graph')

    def adjacent(self, node1, node2):
        ''' Check is if two nodes have an edge connecting them.
            Direction is not important. '''
        try:
            if node2 in self.graph[node1] or node1 in self.graph[node2]:
                return True
            else:
                return False
        except KeyError:
            raise KeyError('node not in graph')

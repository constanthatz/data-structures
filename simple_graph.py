#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Graph(object):
    ''' Create an empty graph. '''
    def __init__(self):
        self.graph = {}

    def nodes(self):
        return self.graph.keys()

    def edges(self):
        edge_list = []
        for key, value in self.graph.iteritems():
            for item in value:
                edge_list.append((key, item))
        return edge_list

    def add_node(self, node):
        self.graph.setdefault(node, [])

    def add_edge(self, node1, node2):
        try:
            self.graph[node1].append(node2)
            if node2 not in self.graph:
                self.add_node(node2)
        except KeyError:
            self.add_node(node1)
            self.graph[node1].append(node2)
            if node2 not in self.graph:
                self.add_node(node2)

    def del_node(self, node):
        try:
            del self.graph[node]
            for value in self.graph.itervalues():
                if node in value:
                    value.remove(node)
        except KeyError:
            raise KeyError('node not in graph')

    def has_node(self, node):
        return node in self.graph

    def neighbors(self, node):
        return self.graph[node]

    def adjecent(self, node1, node2):
        if node2 in self.graph[node1] or node1 in self.graph[node2]:
            return True
        else:
            return False

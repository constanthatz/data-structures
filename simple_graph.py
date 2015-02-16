#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Graph(object):
    ''' Create an empty graph. '''
    def __init__(self):
        self.graph = {}
        return

    def nodes():
        return nodes

    def edges():
        return edges

    def add_node(self, value):
        self.graph.setdefault(value, [])
        return

    def add_edge(self, value1, value2):
        return

    def del_node(self, value):
        try:
            del self.graph[value]
        except KeyError:
            raise KeyError('node not in graph')

    def has_node(self, value):
        return value in self.graph

    def neighbors(self, value):
        return neighbors

    def adjecent(self, value, value2):
        return condition

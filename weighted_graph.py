#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


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
        for key, value in self.graph.iteritems():
            for i, item in enumerate(value['neighbors']):
                return (key, item, value['weights'][i])

    def add_node(self, node):
        ''' Add a node to the graph.
            We are using dictionaries to store neighbors and weights so we
            don't have to loop through lists to remove neighbros and weights.
            '''
        self.graph.setdefault(node, {'neighbors': [], 'weights': []})

    def add_edge(self, node1, node2, weight=0):
        ''' Add an edge to the graph. '''
        # Add node1 to graph
        self.graph.setdefault(node1, {'neighbors': [], 'weights': []})
        # Add edge
        self.graph[node1]['neighbors'].append(node2)
        self.graph[node1]['weights'].append(weight)

        # Check if node1 is in the graph
        if node2 not in self.graph:
            self.add_node(node2)

    def del_edge(self, node1, node2):
        ''' Delete an edge to the graph. '''
        try:
            # Check if node1 exists and node2 is a neighbor and delete the edge
            idx = self.graph[node1]['neighbors'].index(node2)
            self.graph[node1]['neighbors'].remove(node2)
            del self.graph[node1]['weights'][idx]
        except KeyError:
            raise KeyError('node {} not in graph'.format(node1))
        except ValueError:
            raise ValueError('node {} not a neighbor'.format(node2))

    def del_node(self, node):
        ''' Delete a node from the graph. '''
        try:
            del self.graph[node]
            # Delete the node from any neighbor lists it is in.
            for value in self.graph.itervalues():
                    try:
                        value.remove(node)
                    except ValueError:
                        pass
        except KeyError:
            raise KeyError('{} not in graph'.format(node))

    def has_node(self, node):
        ''' Return True or False ifthe node is in the graph or not. '''
        return node in self.graph

    def neighbors(self, node):
        ''' Return the neighbors of a node. '''
        try:
            return self.graph[node]
        except KeyError:
            raise KeyError('{} not in graph'.format(node))

    def adjacent(self, node1, node2):
        ''' Check is if two nodes have an edge connecting them. '''
        try:
            return node2 in self.graph[node1]
        except KeyError:
            raise KeyError('{} not in graph'.format(node1))

if __name__ == '__main__':
    g = Graph()
    g.add_edge(2, 3, 0)
    g.add_edge(4, 5, 5)
    g.add_edge(1, 3, 7)
    g.add_edge(1, 4, 13)
    g.add_edge(1, 5, 2)
    g.edges()

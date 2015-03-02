#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
import stack as stk
import queue as que


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
        return [(key, item, value['weights'][i])
                for key, value in self.graph.iteritems()
                for i, item in enumerate(value['neighbors'])]

    def add_node(self, node):
        ''' Add a node to the graph.
            We are using dictionaries to store neighbors and weights so we
            don't have to loop through lists to remove neighbros and weights.
            '''
        self.graph.setdefault(node, {})

    def add_edge(self, node1, node2, weight=0):
        ''' Add an edge to the graph. '''
        # Add node1 to graph
        self.graph.setdefault(node1, {})
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

if __name__ == "__main__":
    g = Graph()
    g.add_node(3)
    print(g.nodes())
    g.add_edge(4, 8)
    print(g.nodes())
    print(g.neighbors(4))
    print(g.adjacent(4, 8))
    g.del_edge(4, 8)
    print(g.neighbors(4))
    print(g.adjacent(4, 8))

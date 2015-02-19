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
        return [(key, item) for key, value in self.graph.iteritems()
                for item in value]

    def add_node(self, node):
        ''' Add a node to the graph. '''
        self.graph.setdefault(node, [])

    def add_edge(self, node1, node2):
        ''' Add an edge to the graph. '''
        # Add node1 to graph
        self.graph.setdefault(node1, [])
        # Add edge
        self.graph[node1].append(node2)
        # Check if node1 is in the graph
        if node2 not in self.graph:
            self.add_node(node2)

    def del_edge(self, node1, node2):
        ''' Delete an edge to the graph. '''
        try:
            # Check if node1 exists and node2 is a neighbor and delete the edge
            self.graph[node1].remove(node2)
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
            print('The neighbors of {} are {}'.format(
                test_node, self.neighbors(test_node)))

            for neighbor in self.neighbors(test_node):
                print(neighbor)
                print(path)
                if neighbor not in path:
                    print('appending {} to {}'.format(neighbor, path))
                    path.append(neighbor)
                    print(path)
                    queue.enqueue(neighbor)
                    print(queue.front.val)
        return path


if __name__ == '__main__':
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("A", "E")
    g.add_edge("B", "D")
    g.add_edge("B", "F")
    g.add_edge("C", "G")
    g.add_edge("F", "E")
    g.add_edge("E", "A")
    print(g.neighbors("E"))
    print(g.graph["E"])

    path = g.breadth_first_traversal("B")
    # print(path)

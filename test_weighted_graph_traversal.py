#!/usr/bin/env python
from weighted_graph import Graph
import pytest
from collections import OrderedDict as od


@pytest.fixture(scope='function')
def empty_graph():
    return Graph()


@pytest.fixture(scope='function')
def non_empty_graph():
    g = Graph()
    g.add_node("A")
    return g


@pytest.fixture(scope='function')
def edges_graph():
    g = Graph()
    g.add_edge("A", "B", 2)
    return g


@pytest.fixture(scope='function')
def non_multi_connected_nodes_longpath():
    g = Graph()
    g.add_edge("A", "B", 20)
    g.add_edge("A", "C", 2)
    g.add_edge("A", "E", 0)
    g.add_edge("B", "D", 0)
    g.add_edge("B", "F", 0)
    g.add_edge("C", "G", 2)
    g.add_edge("G", "B", 1)
    return g


@pytest.fixture(scope='function')
def non_multi_connected_nodes_shortpath():
    g = Graph()
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 2)
    g.add_edge("A", "E", 0)
    g.add_edge("B", "D", 0)
    g.add_edge("B", "F", 0)
    g.add_edge("C", "G", 2)
    g.add_edge("G", "B", 1)
    return g


@pytest.fixture(scope='function')
def multi_connected_nodes(non_multi_connected_nodes):
    g = non_multi_connected_nodes
    g.add_edge("F", "E")
    return g


@pytest.fixture(scope='function')
def cyclic_graph(multi_connected_nodes):
    g = multi_connected_nodes
    g.add_edge("E", "A")
    return g


@pytest.fixture(scope='function')
def orphan_node(non_multi_connected_nodes):
    g = non_multi_connected_nodes
    g.add_edge("H", "E")
    return g


@pytest.fixture(scope='function')
def childless_orphan_node(non_multi_connected_nodes):
    g = non_multi_connected_nodes
    g.add_node("I")
    return g


def test_simple_edge(edges_graph):
    assert [u'A', u'B'] == edges_graph.dijkstra('A', 'B')
    assert [u'A', u'B'] == edges_graph.FloydWarshall('A', 'B')


def test_empty_graph(empty_graph):
    with pytest.raises(ValueError):
        empty_graph.dijkstra('A', 'B')
        empty_graph.FloydWarshall('A', 'B')


def test_single_node(non_empty_graph):
    with pytest.raises(ValueError):
        non_empty_graph.dijkstra('A', 'B')
        non_empty_graph.FloydWarshall('A', 'B')


def test_longpath(non_multi_connected_nodes_longpath):
    assert [u'A', u'C', u'G', u'B'] == \
        non_multi_connected_nodes_longpath.dijkstra('A', 'B')
    assert [u'A', u'C', u'G', u'B'] == \
        non_multi_connected_nodes_longpath.FloydWarshall('A', 'B')


def test_shortpath(non_multi_connected_nodes_shortpath):
    assert [u'A', u'B'] == \
        non_multi_connected_nodes_shortpath.dijkstra('A', 'B')
    assert [u'A', u'B'] == \
        non_multi_connected_nodes_shortpath.FloydWarshall('A', 'B')

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
def multi_connected_nodes(non_multi_connected_nodes_shortpath):
    g = non_multi_connected_nodes_shortpath
    g.add_edge("F", "E")
    return g


@pytest.fixture(scope='function')
def cyclic_graph(multi_connected_nodes):
    g = multi_connected_nodes
    g.add_edge("E", "A", 0)
    return g


@pytest.fixture(scope='function')
def orphan_node(non_multi_connected_nodes_shortpath):
    g = non_multi_connected_nodes_shortpath
    g.add_edge("H", "E")
    return g


@pytest.fixture(scope='function')
def childless_orphan_node(non_multi_connected_nodes_shortpath):
    g = non_multi_connected_nodes_shortpath
    g.add_node("I")
    return g


def test_simple_edge_dij(edges_graph):
    assert [u'A', u'B'] == edges_graph.dijkstra('A', 'B')


def test_simple_edge_fw(edges_graph):
    assert [u'A', u'B'] == edges_graph.FloydWarshall('A', 'B')


def test_empty_graph_dij(empty_graph):
    with pytest.raises(ValueError):
        empty_graph.dijkstra('A', 'B')


def test_empty_graph_fw(empty_graph):
    with pytest.raises(ValueError):
        empty_graph.FloydWarshall('A', 'B')


def test_single_node_dij(non_empty_graph):
    with pytest.raises(ValueError):
        non_empty_graph.dijkstra('A', 'B')


def test_single_node_fw(non_empty_graph):
    with pytest.raises(ValueError):
        non_empty_graph.FloydWarshall('A', 'B')


def test_longpath_dij(non_multi_connected_nodes_longpath):
    assert [u'A', u'C', u'G', u'B'] == \
        non_multi_connected_nodes_longpath.dijkstra('A', 'B')


def test_longpath_fw(non_multi_connected_nodes_longpath):
    assert [u'A', u'C', u'G', u'B'] == \
        non_multi_connected_nodes_longpath.FloydWarshall('A', 'B')


def test_shortpath_dij(non_multi_connected_nodes_shortpath):
    assert [u'A', u'B'] == \
        non_multi_connected_nodes_shortpath.dijkstra('A', 'B')


def test_shortpath_fw(non_multi_connected_nodes_shortpath):
    assert [u'A', u'B'] == \
        non_multi_connected_nodes_shortpath.FloydWarshall('A', 'B')


def test_cyclic_dij(cyclic_graph):
    assert [u'A'] == cyclic_graph.dijkstra('A', 'A')
    assert [u'A', u'E'] == cyclic_graph.dijkstra('A', 'E')


def test_cyclic_fw(cyclic_graph):
    assert [u'A'] == cyclic_graph.FloydWarshall('A', 'A')
    assert [u'A', u'E'] == cyclic_graph.FloydWarshall('A', 'E')


# def test_childless_orphan_dij(childless_orphan_node):
#     assert [u'I'] == childless_orphan_node.dijkstra('I', 'I')
#     with pytest.raises(IndexError):
#         childless_orphan_node.dijkstra('A', 'I')


def test_childless_orphan_fw(childless_orphan_node):
    assert [u'I'] == childless_orphan_node.FloydWarshall('I', 'I')
    with pytest.raises(IndexError):
        childless_orphan_node.FloydWarshall('A', 'I')

#!/usr/bin/env python
from simple_graph import Graph
import pytest

DFT_A = [u'A', u'E', u'C', u'G', u'B', u'F', u'D']
BFT_A = [u'A', u'B', u'C', u'E', u'D', u'F', u'G']


@pytest.fixture(scope='function')
def empty_graph():
    ''' Define an empty graph. '''
    return Graph()


@pytest.fixture(scope='function')
def non_empty_graph():
    ''' Define an graph with a node. '''
    g = Graph()
    g.add_node("A")
    return g


@pytest.fixture(scope='function')
def edges_graph():
    ''' Define a graph with an edge. '''
    g = Graph()
    g.add_edge("A", "B")
    return g


@pytest.fixture(scope='function')
def non_multi_connected_nodes():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("A", "E")
    g.add_edge("B", "D")
    g.add_edge("B", "F")
    g.add_edge("C", "G")
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


def test_init(empty_graph):
    ''' Test graph creation. '''
    g = empty_graph
    assert g.graph == {}


def test_add_node_empty(empty_graph):
    ''' Test node adding. '''
    # Add to empty graph
    g = empty_graph
    g.add_node("A")
    assert "A" in g.graph
    assert g.graph["A"] == []


def test_add_node_non_empty(non_empty_graph):
    ''' Test node adding. '''
    g = non_empty_graph
    # Add to populated graph
    g.add_node("B")
    assert "B" in g.graph
    assert g.graph["B"] == []


def test_nodes_empty(empty_graph):
    ''' Test node listing. '''
    g = empty_graph
    # Test empty graph
    assert g.nodes() == []


def test_nodes_non_empty(non_empty_graph):
    ''' Test node listing. '''
    g = Graph()
    g.add_node("B")
    # Test populated graph
    assert "A" and "B" in g.graph


def test_add_edge_empty(empty_graph):
    ''' Test adding an edge to graph. '''
    g = empty_graph
    # Add to empty graph
    g.add_edge("A", "B")
    assert "A" in g.graph
    assert "B" in g.graph
    assert "B" in g.graph["A"]


def test_add_edge_existing_node(non_empty_graph):
    ''' Test adding an edge to graph. '''
    # Add edge from existing node
    g = non_empty_graph
    g.add_edge("A", "C")
    assert "C" in g.graph
    assert "C" in g.graph["A"]


def test_add_edge_non_existing_node(non_empty_graph):
    ''' Test adding an edge to graph. '''
    # Add edge from non-existing node
    g = non_empty_graph
    g.add_edge("C", "A")
    assert "C" in g.graph
    assert "A" in g.graph["C"]


def test_add_edge_existing_nodes(non_empty_graph):
    ''' Test addinga edge to graph. '''
    # Add edge between two existing nodes
    g = non_empty_graph
    g.add_node("C")
    g.add_edge("A", "C")
    assert "C" in g.graph["A"]


def test_edges_empty(empty_graph):
    ''' Test edge listing. '''
    g = empty_graph
    # Test empty graph
    assert [] == g.edges()


def test_edges_non_empty(edges_graph):
    g = edges_graph
    # Test non-empty graph
    assert ("A", "B") in g.edges()


def test_del_edge_empty(empty_graph):
    ''' Test deleting an edge from graph. '''
    g = empty_graph
    # Empty graph
    with pytest.raises(KeyError):
        g.del_edge("A", "B")


def test_del_edge_no_neighbors(non_empty_graph):
    ''' Test deleting an edge from graph. '''
    # Node1 doesn't exit
    g = non_empty_graph
    with pytest.raises(KeyError):
        g.del_edge("C", "A")

    # Node2 doesn't exit
    with pytest.raises(ValueError):
        g.del_edge("A", "C")

    # Node2 exists but isn't a neighbor
    g.add_node("B")
    with pytest.raises(ValueError):
        g.del_edge("A", "B")


def test_del_edge(edges_graph):
    ''' Test deleting an edge from graph. '''
    g = edges_graph
    # Both nodes exist and one is a neighbor
    g.del_edge("A", "B")
    assert ("A", "B") not in g.edges()


def test_del_edge_reverse(edges_graph):
    ''' Test deleting an edge from graph. '''
    g = edges_graph
    # Both nodes exist and but the edge is the opposite direction
    with pytest.raises(ValueError):
        g.del_edge("B", "A")
    assert ("A", "B") in g.edges()


def test_del_node(empty_graph):
    ''' Test deleting a node. '''
    g = empty_graph
    # Empty graph
    with pytest.raises(KeyError):
        g.del_node("A")


def test_del_node_unconnected(non_empty_graph):
    ''' Test deleting a node. '''
    g = non_empty_graph
    # Unconnected node
    g.del_node("A")
    assert "A" not in g.graph


def test_del_node_with_neighbor(edges_graph):
    ''' Test delete node with neighbor. '''
    g = edges_graph
    g.del_node("A")
    assert "A" not in g.graph
    assert "B" in g.graph
    assert ("A", "B") not in g.edges()


def test_del_node_neighbor(edges_graph):
    ''' Delete node that is a neighbor '''
    g = edges_graph
    g.del_node("B")
    assert "B" not in g.graph
    assert "A" in g.graph
    assert ("A", "B") not in g.edges()


def test_has_node_empty(empty_graph):
    ''' Test if a node exists in an empty graph. '''
    g = empty_graph
    # Empty graph
    assert g.has_node("A") is False


def test_has_node_non_empty(non_empty_graph):
    ''' Test if a node exists. '''
    g = non_empty_graph
    g.add_node("A")
    assert g.has_node("A") is True
    assert g.has_node("B") is False


def test_neighbors_empty(empty_graph):
    ''' Test neighbor listing of empty graph. '''
    g = empty_graph
    # Empty graph
    with pytest.raises(KeyError):
        g.neighbors("A")


def test_neighbors_non_empty(non_empty_graph):
    ''' Test neighbor listing of an unconnected node. '''
    g = non_empty_graph
    # Node without neighbors
    g.add_node("A")
    assert g.neighbors("A") == []


def test_neighbors_edge(edges_graph):
    ''' Test neighbor listing of a node with an edge. '''
    g = edges_graph
    assert g.neighbors("A") == ["B"]
    # Check that neighbor has not reverse added first node
    assert g.neighbors("B") == []

    # Add additional neighbors
    g.add_edge("A", "C")
    assert g.neighbors("A") == ["B", "C"]

    # Add additional neighbors
    g.add_edge("A", "D")
    assert g.neighbors("A") == ["B", "C", "D"]


def test_adjacent_empty(empty_graph):
    ''' Test if two nodes are adjacent in an empty graph. '''
    g = empty_graph
    with pytest.raises(KeyError):
        g.adjacent("A", "B")


def test_adjacent_non_empty(non_empty_graph):
    ''' Test if two nodes are adjacent in graph with one node. '''
    # First node exists but the other doesn't
    g = non_empty_graph
    assert g.adjacent("A", "B") is False
    # Second node exists but the other doesn't
    with pytest.raises(KeyError):
        g.adjacent("B", "A") is False


def test_adjacent_edge(edges_graph):
    ''' Test if two nodes are adjacent in graph with one node. '''
    # Second node is neighbor to the first, but the first is not neighbor
    # to the second.
    g = edges_graph
    assert g.adjacent("A", "B") is True
    assert g.adjacent("B", "A") is False

    # Second node exists but the other doesn't
    g.add_node("C")
    assert g.adjacent("A", "C") is False


def test_DFT_non(non_multi_connected_nodes):
    # Start at A
    assert DFT_A == non_multi_connected_nodes.depth_first_traversal("A")
    # Start at B
    assert [u'B', u'F', u'D'] == \
        non_multi_connected_nodes.depth_first_traversal("B")
    # Start at G
    assert [u'G'] == \
        non_multi_connected_nodes.depth_first_traversal("G")


def test_DFT_mul(multi_connected_nodes):
    # Start at A
    assert DFT_A == multi_connected_nodes.depth_first_traversal("A")
    # Start at B
    assert [u'B', u'F', u'E', u'D'] == \
        multi_connected_nodes.depth_first_traversal("B")


def test_DFT_cyc(cyclic_graph):
    # Start at A
    assert DFT_A == cyclic_graph.depth_first_traversal("A")
    # Start at B
    assert [u'B', u'F', u'E', u'A', u'C', u'G', u'D'] == \
        cyclic_graph.depth_first_traversal("B")


def test_DFT_orph(orphan_node):
    # Start at A
    assert DFT_A == orphan_node.depth_first_traversal("A")
    # Start at B
    assert [u'H', u'E'] == \
        orphan_node.depth_first_traversal("H")


def test_DFT_corph(childless_orphan_node):
    # Start at A
    assert DFT_A == childless_orphan_node.depth_first_traversal("A")
    # Start at B
    assert [u'I'] == \
        childless_orphan_node.depth_first_traversal("I")


def test_BFT(non_multi_connected_nodes):
    # Start at A
    assert BFT_A == non_multi_connected_nodes.breadth_first_traversal("A")
    # Start at B
    assert [u'B', u'D', u'F'] == \
        non_multi_connected_nodes.breadth_first_traversal("B")


def test_BFT_mul(multi_connected_nodes):
    # Start at A
    assert BFT_A == multi_connected_nodes.breadth_first_traversal("A")
    # Start at B
    assert [u'B', u'D', u'F', u'E'] == \
        multi_connected_nodes.breadth_first_traversal("B")


def test_BFT_cyc(cyclic_graph):
    # Start at A
    assert BFT_A == cyclic_graph.breadth_first_traversal("A")
    # Start at B
    assert [u'B', u'D', u'F', u'E', u'A', u'C', u'G'] == \
        cyclic_graph.breadth_first_traversal("B")


def test_BFT_orph(orphan_node):
    # Start at A
    assert BFT_A == orphan_node.breadth_first_traversal("A")
    # Start at B
    assert [u'B', u'D', u'F'] == \
        orphan_node.breadth_first_traversal("B")


def test_BFT_corph(childless_orphan_node):
    # Start at A
    assert BFT_A == childless_orphan_node.breadth_first_traversal("A")
    # Start at B
    assert [u'B', u'D', u'F'] == \
        childless_orphan_node.breadth_first_traversal("B")

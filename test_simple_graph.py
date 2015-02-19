#!/usr/bin/env python
from simple_graph import Graph
import pytest


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
    g.add_edge("A", "B")
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

    # Delete node with neighbor
    g.add_edge("A", "B")
    g.del_node("A")
    assert "A" not in g.graph
    assert "B" in g.graph
    assert ("A", "B") not in g.edges()

    # Delete node that is a neighbor
    g.add_edge("A", "B")
    g.del_node("B")
    assert "B" not in g.graph
    assert "A" in g.graph
    assert ("A", "B") not in g.edges()


def test_has_node_empty(empty_graph):
    ''' Test if a node exists. '''
    g = empty_graph
    # Empty graph
    assert g.has_node("A") is False

    # Populated graph
    g.add_node("A")
    assert g.has_node("A") is True
    assert g.has_node("B") is False


def test_neighbors_empty(empty_graph):
    ''' Test neighbor listing. '''
    g = empty_graph

    # Empty graph
    with pytest.raises(KeyError):
        g.neighbors("A")

    # Node without neighbors
    g.add_node("A")
    assert g.neighbors("A") == []

    # Node with neighbors after edge
    # # Check that neighbor has not reverse added first node
    g.add_edge("A", "B")
    assert g.neighbors("A") == ["B"]
    assert g.neighbors("B") == []

    # Add additional neighbors
    g.add_edge("A", "C")
    assert g.neighbors("A") == ["B", "C"]

    # Add additional neighbors
    g.add_edge("A", "D")
    assert g.neighbors("A") == ["B", "C", "D"]


def test_adjacent_empty(empty_graph):
    ''' Test if two nodes are adjacent. '''
    g = empty_graph

    # Test empty graph
    with pytest.raises(KeyError):
        g.adjacent("A", "B")

    # First node exists but the other doesn't
    g.add_node("A")
    assert g.adjacent("A", "B") is False

    # Second node is neighbor to the first, but the first is not neighbor
    # to the second.
    g.add_edge("A", "B")
    assert g.adjacent("A", "B") is True
    assert g.adjacent("B", "A") is False

    # Second node exists but the other doesn't
    g.add_node("C")
    assert g.adjacent("A", "C") is False

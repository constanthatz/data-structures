#!/usr/bin/env python
from simple_graph import Graph
import pytest


def test_init():
    ''' Test graph creation. '''
    assert Graph().graph == {}


def test_add_node():
    ''' Test node adding. '''
    g = Graph()
    # Add to empty graph
    g.add_node("A")
    assert "A" in g.graph
    assert g.graph["A"] == []

    # Add to populated graph
    g.add_node("B")
    assert "B" in g.graph
    assert g.graph["B"] == []


def test_nodes():
    ''' Test node listing. '''
    g = Graph()
    # Test empty graph
    assert g.nodes() == []
    g.add_node("A")
    g.add_node("B")
    # Test populated graph
    assert "A" and "B" in g.graph


def test_add_edge():
    ''' Test addinga edge to graph. '''
    g = Graph()
    # Add to empty graph
    g.add_edge("A", "B")
    assert "A" in g.graph
    assert "B" in g.graph
    assert "B" in g.graph["A"]

    # Add edge existing node
    g.add_edge("A", "C")
    assert "C" in g.graph
    assert "C" in g.graph["A"]

    # Add edge non-existing node
    g.add_edge("D", "B")
    assert "D" in g.graph
    assert "B" in g.graph["D"]

    # Add edge between two existing nodes
    g.add_edge("D", "A")
    assert "A" in g.graph["D"]


def test_edges():
    ''' Test edge listing. '''
    g = Graph()
    # Test empty graph
    assert [] == g.edges()
    g.add_edge("A", "B")
    # Add to empty graph
    assert ("A", "B") in g.edges()

    # Add edge non-existing node
    g.add_edge("A", "C")
    assert ("A", "C") in g.edges()

    # Add additional reverse edge between two nodes
    g.add_edge("B", "A")
    assert ("B", "A") in g.edges()

    # Add edge non-existing node
    g.add_edge("D", "B")
    assert ("D", "B") in g.edges()


def test_del_node():
    ''' Test deleting a node. '''
    g = Graph()
    # Empty graph
    with pytest.raises(KeyError):
        g.del_node("A")

    # Unconnected node
    g.add_node("A")
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


def test_has_node():
    ''' Test if a node exists. '''
    g = Graph()
    # Empty graph
    assert g.has_node("A") is False

    # Populated graph
    g.add_node("A")
    assert g.has_node("A") is True
    assert g.has_node("B") is False


def test_neighbors():
    ''' Test neighbor listing. '''
    g = Graph()

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


def test_adjacent():
    ''' Test if two nodes are adjacent. Direction is nor important. '''
    g = Graph()

    # Test empty graph
    with pytest.raises(KeyError):
        g.adjacent("A", "B")

    # First node exists but the other doesn't
    g.add_node("A")
    with pytest.raises(KeyError):
        g.adjacent("A", "B")

    # Second node is neighbor to the first, but the first is not neighbor
    # to the second.
    g.add_edge("A", "B")
    assert g.adjacent("A", "B") is True
    assert g.adjacent("B", "A") is True

    # Second node exists but the other doesn't
    g.add_node("C")
    assert g.adjacent("A", "C") is False

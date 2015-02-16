#!/usr/bin/env python
from simple_graph import Graph
import pytest


def test_init():
    assert Graph().graph == {}


def test_add_node():
    g = Graph()
    g.add_node("A")
    assert "A" in g.graph
    assert g.graph["A"] == []
    g.add_node("B")
    assert "B" in g.graph
    assert g.graph["B"] == []


def test_nodes():
    g = Graph()
    assert g.nodes() == []
    g.add_node("A")
    g.add_node("B")
    assert "A" and "B" in g.graph


def test_add_edge():
    g = Graph()
    g.add_edge("A", "B")
    assert "A" in g.graph
    assert "B" in g.graph
    assert "B" in g.graph["A"]
    g.add_edge("A", "C")
    assert "C" in g.graph
    assert "C" in g.graph["A"]
    g.add_edge("D", "B")
    assert "D" in g.graph
    assert "B" in g.graph["D"]


def test_edges():
    g = Graph()
    assert [] == g.edges()
    g.add_edge("A", "B")
    assert ("A", "B") in g.edges()
    g.add_edge("A", "C")
    assert ("A", "C") in g.edges()
    g.add_edge("B", "A")
    assert ("B", "A") in g.edges()
    g.add_edge("D", "B")
    assert ("D", "B") in g.edges()


def test_del_node():
    g = Graph()
    with pytest.raises(KeyError):
        g.del_node("A")

    g.add_node("A")
    g.del_node("A")
    assert "A" not in g.graph

    g.add_edge("A", "B")
    g.del_node("A")
    assert "A" not in g.graph
    assert "B" in g.graph
    assert ("A", "B") not in g.edges()

    g.add_edge("A", "B")
    g.del_node("B")
    assert "B" not in g.graph
    assert "A" in g.graph
    assert ("A", "B") not in g.edges()


def test_has_node():
    g = Graph()
    assert g.has_node("A") is False
    g.add_node("A")
    assert g.has_node("A") is True
    assert g.has_node("B") is False



# def test_neighbors(value):
#     return neighbors


# def test_adjecent(value, value2):
#     return condition

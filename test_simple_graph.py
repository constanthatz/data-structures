#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from simple_graph import Graph


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


def test_add_edge(value1, value2):


# def test_edges():
#     return edges


# def test_del_node(value):
#     return


# def test_has_node(value):
#     return


# def test_neighbors(value):
#     return neighbors


# def test_adjecent(value, value2):
#     return condition

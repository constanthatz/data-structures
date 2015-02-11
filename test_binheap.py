from __future__ import print_function
import pytest
from binheap import Binheap


def test_init_bh():
    b = Binheap()
    assert b.binlist == []
    c = Binheap([1, 2])
    assert c.binlist == [1, 2]


def test_push_promote_bh():
    b = Binheap()
    b.push(100)
    assert b.binlist == [100]
    b = Binheap([100, 50, 25])
    b.push(30)
    assert b.binlist == [100, 50, 25, 30]
    b = Binheap([100, 50, 25])
    b.push(75)
    assert b.binlist == [100, 75, 25, 50]
    b = Binheap([100, 50, 25])
    b.push(200)
    assert b.binlist == [200, 100, 25, 50]


def test_parent_bh():
    b = Binheap([100, 75, 25, 50])
    assert b._Binheap__parent(3) == [1, 75]


def test_children_bh():
    b = Binheap([100, 75, 25, 50])
    assert b._Binheap__children(0) == [(1, 75), (2, 25)]


def test_battle_children_bh():
    b = Binheap([100, 75, 25, 50])
    children = b._Binheap__children(0)
    assert b._Binheap__battle_children(0, children) == 1


def test_pop_demote_bh():
    b = Binheap([100, 75, 25, 50])
    assert b.pop() == 100
    assert b.binlist == [75, 50, 25]

    b = Binheap([100, 75, 25, 50, 30])
    b.pop()
    assert b.binlist == [75, 50, 25, 30]

    b = Binheap([100, 75, 25, 50, 30, 15])
    assert b.pop() == 100
    assert b.binlist == [75, 50, 25, 15, 30]

    b = Binheap([100, 75, 25, 50, 30, 15, 10])
    assert b.pop() == 100
    assert b.binlist == [75, 50, 25, 10, 30, 15]

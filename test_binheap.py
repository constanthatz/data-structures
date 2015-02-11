import pytest
from binheap import Binheap


def test_init_bh():
    b = Binheap()
    assert b.binlist == []
    c = Binheap([1, 2])
    assert c.binlist == [1, 2]


def test_pushpromote_bh():
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

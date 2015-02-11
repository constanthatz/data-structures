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

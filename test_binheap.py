import pytest
from binheap import Binheap


def test_init_bh():
    b = Binheap()
    assert b.binlist is []
    c = Binheap([1, 2])
    assert c.binlist == [1, 2]

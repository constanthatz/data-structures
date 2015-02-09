from __future__ import unicode_literals
import pytest
from stack import Element
from stack import Stack


def test_element_init():
    m = Element(3)
    assert m.val == 3
    assert m.previous is None

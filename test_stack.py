from __future__ import unicode_literals
import pytest
from stack import Element
from stack import Stack


def test_element_init():
    n = Element()
    assert n.val is None
    assert n.previous is None
    m = Element(3)
    assert m.val == 3
    assert m.previous is None


def test_stack_init():
    l = Stack()
    assert l.top is None


def test_stack_push():
    l = Stack()
    l.push(10)
    assert l.top.val == 10
    assert l.top.previous is None
    l.push("String")
    assert l.top.val == "String"
    assert l.top.previous.val == 10
    assert l.top.previous.previous is None


def test_stack_pop():
    l = Stack()
    l.push(10)
    l.push("String")
    assert l.pop() == "String"
    assert l.top.val == 10
    assert l.top.previous is None
    assert l.pop() == 10
    assert l.top is None
    with pytest.raises(ValueError):
        l.pop()

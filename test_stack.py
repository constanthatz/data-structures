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
    e = Element(10)
    l.push(e)
    assert l.top == e
    assert l.top.previous is None
    f = Element("String")
    l.push(f)
    assert l.top == f
    assert l.top.previous == e
    assert l.top.previous.previous is None


def test_stack_pop():
    l = Stack()
    e = Element(10)
    l.push(e)
    f = Element("String")
    l.push(f)
    assert l.pop() == f.val
    assert l.top == e
    assert l.top.previous is None
    assert l.pop() == e.val
    assert l.top is None
    with pytest.raises(ValueError):
        l.pop()

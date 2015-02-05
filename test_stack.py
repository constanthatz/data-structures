import pytest
from stack import Element
from stack import Stack


def test_element_init():
    n = Element()
    assert n.val is None
    assert n.next is None
    n = Element(3)
    assert n.val == 3
    assert n.next is None


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


# def test_stack_pop():
#     l = stack()
#     a = l.pop()
#     assert a is None

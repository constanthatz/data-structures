from priorityq import Element
from priorityq import Priorityq
import pytest


def que(queue):
    que = []
    current = queue.front
    while current:
        que = [current.val] + que
        current = current.behind
    return que


def test_element_init():
    m = Element(3, 3)
    assert m.val == 3
    assert m.behind is None
    assert m.prio == 3


def test_prioq_init():
    l = Priorityq()
    assert l.front is None


def test_priorityq_prio():
    l = Priorityq()
    l.insert("Nick", 1)
    ql = que(l)
    assert l.front.val == "Nick"
    assert ql == ["Nick"]

    l.insert("Constantine", 1)
    ql = que(l)
    assert l.front.val == "Nick"
    assert ql == ["Constantine", "Nick"]

    l.insert("Mark", 2)
    ql = que(l)
    assert l.front.val == "Mark"
    assert ql == ["Constantine", "Nick",  "Mark"]

    l.insert("Henry", 2)
    ql = que(l)
    assert l.front.val == "Mark"
    assert l.front.behind.val == "Henry"
    assert ql == ["Constantine", "Nick", "Henry", "Mark"]

    l.insert("Jake", 3)
    ql = que(l)
    assert ql == ["Constantine", "Nick", "Henry", "Mark", "Jake"]

    l.insert("James", 0)
    ql = que(l)
    assert ql == ["James", "Constantine", "Nick", "Henry", "Mark", "Jake"]


def test_prioq_pop():
    l = Priorityq()
    with pytest.raises(IndexError):
        l.pop()

    l = Priorityq()
    l.insert("Nick", 1)
    assert l.pop() == 'Nick'
    assert l.front is None
    assert l.back is None

    l = Priorityq()
    l.insert("Mark", 2)
    l.insert("Henry", 2)
    assert l.pop() == "Mark"
    assert l.front.val == "Henry"


def test_prioq_peek():
    l = Priorityq()
    with pytest.raises(IndexError):
        l.peek()

    l = Priorityq()
    l.insert("Nick", 1)
    assert l.peek() == 'Nick'

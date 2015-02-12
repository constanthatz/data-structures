from priorityq import Element
from priorityq import Priorityq


def que(queue):
    que = []
    current = queue.back
    while current:
        que.append(current.val)
        current = current.ahead
    return que


def test_element_init():
    m = Element(3, 3)
    assert m.val == 3
    assert m.behind is None
    assert m.ahead is None
    assert m.prio == 3


def test_prioq_init():
    l = Priorityq()
    assert l.front is None
    assert l.back is None


def test_priorityq_prio():
    l = Priorityq()
    l.insert("Nick", 1)
    ql = que(l)
    assert l.front.val == "Nick"
    assert l.back.val == "Nick"
    assert ql == ["Nick"]

    l.insert("Constantine", 1)
    ql = que(l)
    assert l.front.val == "Nick"
    assert l.back.val == "Constantine"
    assert ql == ["Constantine", "Nick"]

    l.insert("Mark", 2)
    ql = que(l)
    assert l.front.val == "Mark"
    assert l.back.val == "Constantine"
    assert l.back.ahead.val == "Nick"
    assert ql == ["Constantine", "Nick",  "Mark"]


    l.insert("Henry", 2)
    ql = que(l)
    assert l.front.val == "Mark"
    assert l.front.behind.val == "Henry"
    assert l.back.val == "Constantine"
    assert ql == ["Constantine", "Nick", "Henry", "Mark"]

    l.insert("Jake", 3)
    ql = que(l)
    assert ql == ["Constantine", "Nick", "Henry", "Mark", "Jake"]

    l.insert("James", 0)
    ql = que(l)
    assert ql == ["James", "Constantine", "Nick", "Henry", "Mark", "Jake"]

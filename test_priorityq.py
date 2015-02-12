from priorityq import Element
from priorityq import Priorityq


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
    assert l.front.val == "Nick"
    assert l.back.val == "Nick"

    l.insert("Constantine", 1)
    assert l.front.val == "Nick"
    assert l.back.val == "Constantine"

    l.insert("Mark", 2)
    assert l.front.val == "Mark"
    assert l.back.val == "Constantine"

    l.insert("Henry", 2)
    assert l.front.val == "Mark"
    assert l.front.behind.val == "Henry"
    assert l.back.val == "Constantine"

    l.insert("Jake", 3)
    l.insert("James", 0)

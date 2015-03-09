from priorityq import Element
from priorityq import Priorityq
import pytest


@pytest.fixture(scope="function")
def empty_queue():
    pqueue = Priorityq()
    return pqueue


@pytest.fixture(scope="function")
def one_queue():
    pqueue = Priorityq()
    pqueue.insert("Nick", 5)
    return pqueue


def test_element_init():
    m = Element(3, 3)
    assert m.val == 3
    assert m.prio == 3


def test_prioq_init(empty_queue):
    assert empty_queue.binlist == []


def test_priorityq_insert(one_queue):
    assert one_queue.binlist[0].val == "Nick"
    assert one_queue.binlist[0].prio == 5


def test_priorityq_insert_equal(one_queue):
    one_queue.insert("Constantine", 1)
    assert [one_queue.binlist[0].val,
            one_queue.binlist[1].val] == ["Nick", "Constantine"]


def test_priorityq_insert_lower(one_queue):
    one_queue.insert("Constantine", 1)
    assert [one_queue.binlist[0].val,
            one_queue.binlist[1].val] == ["Nick", "Constantine"]


def test_priorityq_insert_higher(one_queue):
    one_queue.insert("Constantine", 10)
    assert [one_queue.binlist[0].val,
            one_queue.binlist[1].val] == ["Constantine", "Nick"]

#     l.insert("Mark", 2)
#     ql = que(l)
#     assert l.front.val == "Mark"
#     assert ql == ["Constantine", "Nick",  "Mark"]

#     l.insert("Henry", 2)
#     ql = que(l)
#     assert l.front.val == "Mark"
#     assert l.front.behind.val == "Henry"
#     assert ql == ["Constantine", "Nick", "Henry", "Mark"]

#     l.insert("Jake", 3)
#     ql = que(l)
#     assert ql == ["Constantine", "Nick", "Henry", "Mark", "Jake"]

#     l.insert("James", 0)
#     ql = que(l)
#     assert ql == ["James", "Constantine", "Nick", "Henry", "Mark", "Jake"]


# def test_prioq_pop():
#     l = Priorityq()
#     with pytest.raises(IndexError):
#         l.pop()

#     l = Priorityq()
#     l.insert("Nick", 1)
#     assert l.pop() == 'Nick'
#     assert l.front is None
#     assert l.back is None

#     l = Priorityq()
#     l.insert("Mark", 2)
#     l.insert("Henry", 2)
#     assert l.pop() == "Mark"
#     assert l.front.val == "Henry"


# def test_prioq_peek():
#     l = Priorityq()
#     with pytest.raises(IndexError):
#         l.peek()

#     l = Priorityq()
#     l.insert("Nick", 1)
#     assert l.peek() == 'Nick'

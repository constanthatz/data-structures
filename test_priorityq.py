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


def test_prioq_pop_empty(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.pop()


def test_prioq_pop(one_queue):
    assert one_queue.pop() == 'Nick'
    assert one_queue.binlist == []


def test_prioq_peek_empty(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.peek()


def test_prioq_peek(one_queue):
    assert one_queue.peek() == 'Nick'

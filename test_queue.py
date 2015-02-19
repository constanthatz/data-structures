from __future__ import unicode_literals
import pytest
from queue import Element
from queue import Queue


@pytest.fixture(scope='function')
def empty_queue():
    return Queue()


@pytest.fixture(scope='function')
def non_empty_queue():
    l = Queue()
    l.enqueue(10)
    return l


def test_element_init():
    ''' Test Element init. '''
    m = Element(3)
    assert m.val == 3
    assert m.behind is None


def test_queue_init(empty_queue):
    ''' Test Queue init. '''
    assert empty_queue.front is None
    assert empty_queue.back is None


def test_enqueue_empty(empty_queue):
    ''' Test enqueue method. '''
    empty_queue.enqueue(10)
    assert empty_queue.front.val == 10
    assert empty_queue.back.val == 10
    assert empty_queue.front is empty_queue.back


def test_enqueue_non_empty(non_empty_queue):
    ''' Test enqueue method on non-empty queue. '''
    non_empty_queue.enqueue("String")
    assert non_empty_queue.front.val == 10
    assert non_empty_queue.front.behind.val == "String"


def test_dequeue_empty(empty_queue):
    ''' Test dequeue method. '''
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_dequeue_empty_one(non_empty_queue):
    ''' Test dequeue method. '''
    assert non_empty_queue.dequeue() == 10
    assert non_empty_queue.front is None
    assert non_empty_queue.back is None


def test_dequeue_non_empty(non_empty_queue):
    ''' Test dequeue on non-empty queue. '''
    non_empty_queue.enqueue("String")
    assert non_empty_queue.dequeue() == 10
    assert non_empty_queue.front.val == "String"


def test_size_empty(empty_queue):
    ''' Test size method. '''
    assert empty_queue.size() == 0


def test_size_non_empty(non_empty_queue):
    ''' Test size on non-empty queue. '''
    non_empty_queue.enqueue("String")
    assert non_empty_queue.size() == 2
    non_empty_queue.dequeue()
    assert non_empty_queue.size() == 1

from __future__ import unicode_literals
import pytest
from queue import Element
from queue import Queue


def test_element_init():
    ''' Test Element init. '''
    m = Element(3)
    assert m.val == 3
    assert m.behind is None


def test_queue_init():
    ''' Test Queue init. '''
    l = Queue()
    assert l.front is None
    assert l.back is None


def test_enqueue():
    ''' Test enqueue method. '''
    l = Queue()
    l.enqueue(10)
    assert l.front.val == 10
    assert l.back.val == 10
    assert l.front is l.back


def test_enqueue_non_empty():
    ''' Test enqueue method on non-empty queue. '''
    l = Queue()
    l.enqueue(10)
    l.enqueue("String")
    assert l.front.val == 10
    assert l.front.behind.val == "String"


def test_dequeue():
    ''' Test dequeue method. '''
    l = Queue()
    with pytest.raises(IndexError):
        l.dequeue()


def test_dequeue_non_empty():
    ''' Test dequeue on non-empty queue. '''
    l = Queue()
    l.enqueue(10)
    l.enqueue("String")
    assert l.dequeue() == 10
    assert l.front.val == "String"


def test_size():
    ''' Test size method. '''
    l = Queue()
    assert l.size() == 0


def test_size_non_empty():
    ''' Test size on non-empty queue. '''
    l = Queue()
    l.enqueue(10)
    l.enqueue("String")
    assert l.size() == 2
    l.dequeue()
    assert l.size() == 1

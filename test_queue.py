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


def test_queue_enqueue():
    ''' Test enqueue method. '''
    l = Queue()

    ''' Test enqueue to empty queue '''
    l.enqueue(10)
    ''' Check front element value and pointers. '''
    assert l.front.ahead is None
    assert l.front.val == 10
    assert l.front.behind is None

    ''' Check back element value and pointers. '''
    assert l.back.ahead is None
    assert l.back.val == 10
    assert l.back.behind is None

    ''' Check that front element is the back element. '''
    assert l.front is l.back

    ''' Test queue of two elements '''
    l.enqueue("String")
    ''' Check front element value and pointers. '''
    assert l.front.ahead is None
    assert l.front.val == 10
    assert l.front.behind.val == "String"

    ''' Check back element value and pointers. '''
    assert l.back.ahead.val == 10
    assert l.back.val == "String"
    assert l.back.behind is None

    ''' Check that front element and back elements point at each other. '''
    assert l.back.ahead == l.front
    assert l.front.behind == l.back

    ''' Test queue of three elements '''
    l.enqueue([])

    ''' Check that front and back elements point too the same element. '''
    assert l.front.behind == l.back.ahead

    ''' Check middle element value and pointers. '''
    assert l.back.ahead.ahead is l.front
    assert l.back.ahead.val == "String"
    assert l.back.ahead.behind is l.back


def test_queue_dequeue():
    ''' Test dequeue method. '''
    l = Queue()

    ''' Test dequeue on empty queue. '''
    with pytest.raises(IndexError):
        l.dequeue()

    ''' Test dequeue on non-empty queue. '''
    l.enqueue(10)
    l.enqueue("String")
    l.enqueue([])

    ''' Check return of dequeue. '''
    assert l.dequeue() == 10

    ''' Check that front of queue has be reassigned. '''
    assert l.front.ahead is None
    assert l.front.val == "String"
    assert l.front.behind.val == []


def test_Queue_size():
    ''' Test size method. '''
    l = Queue()

    ''' Test size on empty queue. '''
    assert l.size() == 0

    ''' Test size on non-empty queue. '''
    l.enqueue('Bob')
    l.enqueue(32)
    l.enqueue('Things')
    assert l.size() == 3

    ''' Test size on non-empty queue that has been dequeued. '''
    l.dequeue()
    assert l.size() == 2

from __future__ import unicode_literals
import pytest
from queue import Element
from queue import Queue


def test_element_init():
    m = Element(3)
    assert m.val == 3
    assert m.behind is None


def test_queue_init():
    l = Queue()
    assert l.front is None
    assert l.back is None


def test_queue_enqueue():
    l = Queue()
    l.enqueue(10)
    assert l.front.val == 10
    assert l.front.behind is None
    assert l.front.ahead is None
    assert l.back.val == 10
    assert l.back.ahead is None
    assert l.back.behind is None
    l.enqueue("String")
    assert l.front.val == 10
    assert l.front.behind.val == "String"
    assert l.front.ahead is None
    assert l.back.val == "String"
    assert l.back.ahead.val == 10
    assert l.back.behind is None
    assert l.front == l.back.ahead
    assert l.front.behind == l.back
    l.enqueue("Third")
    assert l.front.val == 10
    assert l.front.behind.val is "String"
    assert l.front.ahead is None
    assert l.back.val == "Third"
    assert l.back.ahead.val == "String"
    assert l.back.behind is None
    assert l.front.behind == l.back.ahead
    assert l.front.behind.behind == l.back
    assert l.back.ahead.ahead == l.front

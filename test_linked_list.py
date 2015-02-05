import pytest
from linked_list import Node
from linked_list import LinkedList


def test_init():
    l = LinkedList()

    assert l.head == None


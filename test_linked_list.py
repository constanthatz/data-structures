import pytest
from linked_list import Node
from linked_list import LinkedList


def test_node_init():
    n = Node(3)

    assert n.val == 3
    assert n.next is None


def test_linkedlist_init():
    l = LinkedList()
    assert l.head is None


def test_linkedlist_repr():
    l = LinkedList()
    assert repr(l) == '()'


def test_linkedlist_insert():
    l = LinkedList()
    l.insert('Bob')
    l.insert(32)
    assert l.head.val == 32
    assert l.head.next.val == 'Bob'


def test_linkedlist_pop():
    l = LinkedList()
    l.insert('Bob')
    l.insert(32)
    l.pop()
    assert l.head.val == 'Bob'


def test_linkedlist_size():
    l = LinkedList()
    l.insert('Bob')
    l.insert(32)
    l.insert('Things')
    assert l.size() == 3
    l.pop()
    assert l.size() == 2


def test_linkedlist_search():
    l = LinkedList()
    l.insert('Bob')
    l.insert(32)
    assert l.search(32) == l.head
    assert l.search('Bob') == l.head.next


def test_linkedlist_remove():
    l = LinkedList()
    l.insert('Bob')
    l.insert(32)
    l.insert('Things')
    assert l.size() == 3
    l.remove(l.search(32))
    assert l.search(32) is None
    assert l.size() == 2

    l.remove(l.search('Things'))
    assert l.search('Things') is None
    assert l.size() == 1

    l.remove(l.search('Bob'))
    assert l.search('Bob') is None
    assert l.size() == 0



def test_linkedlist_display(capsys):
    l = LinkedList()
    l.insert('Bob')
    l.insert(32)
    l.insert('Things')
    l.display()
    out, err = capsys.readouterr()
    assert out == "('Things', 32, 'Bob')\n"

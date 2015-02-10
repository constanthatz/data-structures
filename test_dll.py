from __future__ import unicode_literals
import pytest
from dll import Node
from dll import DLL


def test_node_init():
    ''' Test node init. '''
    m = Node(3)
    assert m.val == 3
    assert m.behind is None


def test_dll_init():
    ''' Test dll init. '''
    l = DLL()
    assert l.head is None
    assert l.tail is None


def test_dll_append():
    ''' Test append method. '''
    l = DLL()

    ''' Test append to empty dll '''
    l.append(10)
    ''' Check head element value and pointers. '''
    assert l.head.ahead is None
    assert l.head.val == 10
    assert l.head.behind is None

    ''' Check tail element value and pointers. '''
    assert l.tail.ahead is None
    assert l.tail.val == 10
    assert l.tail.behind is None

    ''' Check that head element is the tail element. '''
    assert l.head is l.tail

    ''' Test dll of two elements '''
    l.append("String")
    ''' Check head element value and pointers. '''
    assert l.head.ahead is None
    assert l.head.val == 10
    assert l.head.behind.val == "String"

    ''' Check tail element value and pointers. '''
    assert l.tail.ahead.val == 10
    assert l.tail.val == "String"
    assert l.tail.behind is None

    ''' Check that head element and tail elements point at each other. '''
    assert l.tail.ahead == l.head
    assert l.head.behind == l.tail

    ''' Test dll of three elements '''
    l.append([])

    ''' Check that head and tail elements point too the same element. '''
    assert l.head.behind == l.tail.ahead

    ''' Check middle element value and pointers. '''
    assert l.tail.ahead.ahead is l.head
    assert l.tail.ahead.val == "String"
    assert l.tail.ahead.behind is l.tail


def test_dll_shift():
    ''' Test shift method. '''
    l = DLL()

    ''' Test shift on empty dll. '''
    with pytest.raises(IndexError):
        l.shift()

    ''' Test shift on non-empty dll. '''
    l.append(10)
    l.append("String")
    l.append([1, "string"])

    ''' Check return of shift. '''
    assert l.shift() == [1, "string"]

    ''' Check that tail of dll has be reassigned. '''
    assert l.tail.ahead.val == 10
    assert l.tail.val == "String"
    assert l.tail.behind is None


def test_dll_insert():
    ''' Test insert method. '''
    l = DLL()

    ''' Test insert to empty dll '''
    l.insert(10)
    ''' Check tail element value and pointers. '''
    assert l.tail.behind is None
    assert l.tail.val == 10
    assert l.tail.ahead is None

    ''' Check head element value and pointers. '''
    assert l.head.behind is None
    assert l.head.val == 10
    assert l.head.ahead is None

    ''' Check that tail element is the head element. '''
    assert l.tail is l.head

    ''' Test dll of two elements '''
    l.insert("String")
    ''' Check tail element value and pointers. '''
    assert l.tail.behind is None
    assert l.tail.val == 10
    assert l.tail.ahead.val == "String"

    ''' Check head element value and pointers. '''
    assert l.head.behind.val == 10
    assert l.head.val == "String"
    assert l.head.ahead is None

    ''' Check that tail element and head elements point at each other. '''
    assert l.head.behind == l.tail
    assert l.tail.ahead == l.head

    ''' Test dll of three elements '''
    l.insert([])

    ''' Check that tail and head elements point to the same element. '''
    assert l.tail.ahead == l.head.behind

    ''' Check middle element value and pointers. '''
    assert l.head.behind.behind is l.tail
    assert l.head.behind.val == "String"
    assert l.head.behind.ahead is l.head


def test_dll_pop():
    ''' Test pop method. '''
    l = DLL()

    ''' Test pop on empty dll. '''
    with pytest.raises(IndexError):
        l.pop()

    ''' Test pop on non-empty dll. '''
    l.insert(10)
    l.insert("String")
    l.insert([1, "string"])

    ''' Check return of pop. '''
    assert l.pop() == [1, "string"]

    ''' Check that head of dll has be reassigned. '''
    assert l.head.behind.val == 10
    assert l.head.val == "String"
    assert l.head.ahead is None


def test_dll_remove():
    ''' Test remove method. '''
    l = DLL()

    ''' Test remove on empty dll. '''
    with pytest.raises(ValueError):
        l.remove("val")

    ''' Test remove on non-empty dll. '''
    l.insert(10)
    l.insert("String")
    l.insert(5)
    l.insert("Other")
    l.insert([1, "string"])

    ''' Test removing middle '''
    l.remove(5)
    assert l.tail.ahead.ahead.val == "Other"
    assert l.head.behind.behind.val == "String"

    ''' Test removing the head '''
    l.remove([1, "string"])
    assert l.head.val == "Other"

    ''' Test removing the tail '''
    l.remove(10)
    assert l.tail.val == "String"

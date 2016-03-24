from __future__ import unicode_literals
import pytest
from dll import Node
from dll import DLL


@pytest.fixture(scope='function')
def empty_dll():
    return DLL()


@pytest.fixture(scope='function')
def one_dll():
    l = DLL()
    l.append(10)
    return l


@pytest.fixture(scope='function')
def two_dll():
    l = DLL()
    l.append(10)
    l.append('String')
    return l


@pytest.fixture(scope='function')
def three_dll():
    l = DLL()
    l.append(10)
    l.append('String')
    l.append([])
    return l


def test_node_init():
    ''' Test node init. '''
    m = Node(3)
    assert m.val == 3
    assert m.behind is None


def test_dll_init(empty_dll):
    ''' Test dll init. '''
    assert empty_dll.head is None
    assert empty_dll.tail is None


def test_dll_append_empty_head(empty_dll):
    ''' Test append to empty dll '''
    empty_dll.append(10)
    ''' Check head element value and pointers. '''
    assert empty_dll.head.ahead is None
    assert empty_dll.head.val == 10
    assert empty_dll.head.behind is None


def test_dll_append_empty_tail(empty_dll):
    ''' Test append to empty dll '''
    empty_dll.append(10)
    ''' Check tail element value and pointers. '''
    assert empty_dll.tail.ahead is None
    assert empty_dll.tail.val == 10
    assert empty_dll.tail.behind is None


def test_dll_append_empty_head_tail(empty_dll):
    ''' Test append to empty dll '''
    empty_dll.append(10)
    ''' Check that head element is the tail element. '''
    assert empty_dll.head is empty_dll.tail


def test_dll_append_one_head(one_dll):
    ''' Test append to empty dll '''
    one_dll.append("String")
    ''' Check head element value and pointers. '''
    assert one_dll.head.ahead is None
    assert one_dll.head.val == 10
    assert one_dll.head.behind.val == "String"


def test_dll_append_one_tail(one_dll):
    ''' Test append to empty dll '''
    one_dll.append("String")
    ''' Check tail element value and pointers. '''
    assert one_dll.tail.ahead.val == 10
    assert one_dll.tail.val == "String"
    assert one_dll.tail.behind is None


def test_dll_append_one_head_tail(one_dll):
    ''' Test append to empty dll '''
    one_dll.append("String")
    ''' Check that head element and tail elements point at each other. '''
    assert one_dll.tail.ahead == one_dll.head
    assert one_dll.head.behind == one_dll.tail


def test_dll_append_two_head_tail(two_dll):
    ''' Test dll of three elements '''
    two_dll.append([])
    ''' Check that head and tail elements point too the same element. '''
    assert two_dll.head.behind == two_dll.tail.ahead


def test_dll_append_two_middle(two_dll):
    ''' Test dll of three elements '''
    two_dll.append([])
    ''' Check middle element value and pointers. '''
    assert two_dll.tail.ahead.ahead is two_dll.head
    assert two_dll.tail.ahead.val == "String"
    assert two_dll.tail.ahead.behind is two_dll.tail


def test_dll_shift_empty(empty_dll):
    ''' Test shift on empty dll. '''
    with pytest.raises(IndexError):
        empty_dll.shift()


def test_dll_shift_non_empty(two_dll):
    ''' Test shift on non-empty dll. '''
    ''' Check return of shift. '''
    assert two_dll.shift() == 'String'


def test_dll_shift_non_empty_tail(two_dll):
    ''' Test shift on non-empty dll. '''
    ''' Check that tail of dll has be reassigned. '''
    two_dll.shift()
    assert two_dll.tail.val == 10


def test_dll_insert_empty_tail(empty_dll):
    ''' Test insert to empty dll '''
    empty_dll.insert(10)
    ''' Check tail element value and pointers. '''
    assert empty_dll.tail.behind is None
    assert empty_dll.tail.val == 10
    assert empty_dll.tail.ahead is None


def test_dll_insert_empty_head(empty_dll):
    ''' Test insert to empty dll '''
    empty_dll.insert(10)
    ''' Check head element value and pointers. '''
    assert empty_dll.head.behind is None
    assert empty_dll.head.val == 10
    assert empty_dll.head.ahead is None


def test_dll_insert_empty_head_tail(empty_dll):
    ''' Test insert to empty dll '''
    empty_dll.insert(10)
    ''' Check that tail element is the head element. '''
    assert empty_dll.tail is empty_dll.head


def test_dll_insert_non_empty_tail(one_dll):
    ''' Test dll of two elements '''
    one_dll.insert("String")
    ''' Check tail element value and pointers. '''
    assert one_dll.tail.behind is None
    assert one_dll.tail.val == 10
    assert one_dll.tail.ahead.val == "String"


def test_dll_insert_non_empty_head(one_dll):
    ''' Test dll of two elements '''
    one_dll.insert("String")
    ''' Check head element value and pointers. '''
    assert one_dll.head.behind.val == 10
    assert one_dll.head.val == "String"
    assert one_dll.head.ahead is None


def test_dll_insert_non_empty_head_tail(one_dll):
    ''' Test dll of two elements '''
    one_dll.insert("String")
    ''' Check that tail element and head elements point at each other. '''
    assert one_dll.head.behind == one_dll.tail
    assert one_dll.tail.ahead == one_dll.head


def test_dll_insert_non_empty_2nodes_head_tail(two_dll):
    two_dll.insert([])
    ''' Check that tail and head elements point to the same element. '''
    assert two_dll.tail.ahead == two_dll.head.behind


def test_dll_insert_non_empty_2nodes_middle(two_dll):
    two_dll.insert([])
    ''' Check middle element value and pointers. '''
    assert two_dll.head.behind.behind is two_dll.tail
    assert two_dll.head.behind.val == 10
    assert two_dll.head.behind.ahead is two_dll.head


def test_dll_pop_empty(empty_dll):
    ''' Test pop on empty dll. '''
    with pytest.raises(IndexError):
        empty_dll.pop()


def test_dll_pop_non_empty(two_dll):
    ''' Test pop on non-empty dll. '''
    ''' Check return of pop. '''
    assert two_dll.pop() == 10


def test_dll_pop_non_empty_head(two_dll):
    ''' Check that head of dll has be reassigned. '''
    two_dll.pop()
    assert two_dll.head.behind is None
    assert two_dll.head.val == 'String'
    assert two_dll.head.ahead is None


def test_dll_remove(empty_dll):
    ''' Test remove on empty dll. '''
    with pytest.raises(ValueError):
        empty_dll.remove("val")


def test_dll_remove_non_empty_middle(three_dll):
    ''' Test removing middle '''
    three_dll.remove('String')
    assert three_dll.tail.ahead.val == 10
    assert three_dll.head.behind.val == []


def test_dll_remove_non_empty_head(three_dll):
    ''' Test removing the head '''
    three_dll.remove(10)
    assert three_dll.head.val == 'String'


def test_dll_remove_non_empty_tail(three_dll):
    ''' Test removing the tail '''
    three_dll.remove([])
    assert three_dll.tail.val == 'String'

from __future__ import print_function
import pytest
from binheap import Binheap


@pytest.fixture(scope='function')
def empty_heap():
    return Binheap()


@pytest.fixture(scope='function')
def small_heap():
    return Binheap([100, 50, 25])


@pytest.fixture(scope='function')
def big_heap():
    return Binheap([100, 75, 25, 50])


@pytest.fixture(scope='function')
def bigger_heap():
    return Binheap([100, 75, 25, 50, 30])


@pytest.fixture(scope='function')
def biggest_heap():
    return Binheap([100, 75, 25, 50, 30, 15])


def test_init_bh_empty(empty_heap):
    ''' Create empty heap. '''
    assert empty_heap.binlist == []


def test_init_bh_non_empty(small_heap):
    ''' Create heap with values. '''
    assert small_heap.binlist == [100, 50, 25]


def test_push_promote_bh_empty(empty_heap):
    ''' Push on empty heap. '''
    empty_heap.push(100)
    assert empty_heap.binlist == [100]


def test_push_promote_bh_non_empty_small(small_heap):
    ''' Push small value on heap. '''
    small_heap.push(30)
    assert small_heap.binlist == [100, 50, 25, 30]


def test_push_promote_bh_non_empty_middle(small_heap):
    ''' Push middle value on heap. '''
    small_heap.push(75)
    assert small_heap.binlist == [100, 75, 25, 50]


def test_push_promote_bh_non_empty_high(small_heap):
    ''' Push high value on heap. '''
    small_heap.push(200)
    assert small_heap.binlist == [200, 100, 25, 50]


def test_parent_bh(big_heap):
    ''' Test find parents. '''
    assert big_heap._parent(3) == [1, 75]


def test_children_bh(big_heap):
    ''' Test find children. '''
    assert big_heap._children(0) == [(1, 75), (2, 25)]


def test_battle_children_bh(big_heap):
    ''' Test compare children. '''
    children = big_heap._children(0)
    assert big_heap._battle_children(0, children) == 1


def test_pop_demote_bh(big_heap):
    ''' Test popping top of heap. '''
    assert big_heap.pop() == 100
    assert big_heap.binlist == [75, 50, 25]


def test_pop_demote_bh_bigger(bigger_heap):
    ''' Test popping top of heap. '''
    assert bigger_heap.pop() == 100
    assert bigger_heap.binlist == [75, 50, 25, 30]


def test_pop_demote_bh_biggest(biggest_heap):
    assert biggest_heap.pop() == 100
    assert biggest_heap.binlist == [75, 50, 25, 15, 30]

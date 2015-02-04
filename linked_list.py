#!/usr/bin/env python
from __future__ import print_function


class Node(object):

    def __init__(self, value):
        self._val = value
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def val(self):
        return self._val


class LinkedList(object):

    def __init__(self):
        self._head = None
        self.second = None

    def insert(self, val):
        self.second, self._head = self._head, Node(val)
        self._head.next = self.second

    @property
    def head(self):
        return self._head


l = LinkedList()
l.insert('Nick')
l.insert('Constantine')
print(l.head.val)
print(l.head.next.val)

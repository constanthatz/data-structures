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

    def pop(self):
        self._head = self._head.next

    def size(self):
        if not self._head:
            return 0
        else:
            i = 0
            z = 1
            try:
                a = self._head.next
            except AttributeError:
                return i
            while z != 0:
                try:
                    a = a.next
                except AttributeError:
                    z = 0
                i += 1
            return i

    @property
    def head(self):
        return self._head

l = LinkedList()
l.insert('Nick')
print(l.size())

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

    @property
    def head(self):
        return self._head

    def insert(self, val):
        if not self._head:
            self._head = Node(val)
            self._head.next = None
        else:
            self._head.next, self._head = Node(val), self._head

    def pop(self):
        self._head = self._head.next

    def size(self):
        if not self._head:
            return 0
        else:
            i = 1
            if not self._head.next:
                return i
            else:
                a = self._head.next
                z = 1
                while z:
                    i += 1
                    try:
                        a = a.next
                    except AttributeError:
                        z = 0
                return i

l = LinkedList()
l.insert('Nick')
l.insert('Constantine')
l.insert('Maria')
print(l.size())

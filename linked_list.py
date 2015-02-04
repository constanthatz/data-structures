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
            b = self._head
            self._head = Node(val)
            self._head.next = b

    def pop(self):
        self._head = self._head.next

    def size(self):
        i = 0
        if not self._head:
            return i
        else:
            i = 1
            if not self._head.next:
                return i
            else:
                i = 2
                z = 1
                a = self._head.next
                while z:
                    if not a.next:
                        z = 0
                        return i
                    else:
                        a = a.next
                        i += 1

    # def search

l = LinkedList()
# l.insert('Nick')
# l.insert('Constantine')

# l.insert('Maria')
# l.insert('Bob')
print(l.size())

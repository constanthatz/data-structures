#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Node(object):

    def __init__(self, value):
        self._val = value
        self._next = None


class LinkedList(object):

    def __init__(self):
        self._head = None

    def insert(self, val):
        if not self._head:
            self._head = Node(val)
            self._head.next = None
        else:
            b = self._head
            self._head = Node(val)
            self._head.next = b

    def pop(self):
        if not self._head:
            return None
        else:
            val = self._head.val
            self._head = self._head.next
            return val

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

    def search(self, value):
        z = 1
        a = self._head
        while z:
            if not a:
                z = 0
                return None
            elif a.val == value:
                z = 0
                return a
            elif not a.next:
                z = 0
                return None
            else:
                a = a.next

    def remove(self, node):
        z = 1
        a = self._head
        while z:
            if self._head == node:
                z = 0
                self._head = self._head.next
            elif not a.next:
                z = 0
            elif a.next == node:
                z = 0
                a.next = node.next
            else:
                a = a.next

    def display(self):
        print(repr(self))

    def __repr__(self):
        z = 1
        a = self._head
        node_list = "("
        while z:
            if not a:
                z = 0
                node_list += ")"
            elif isinstance(a.val, str) or isinstance(a.val, unicode):
                if not a.next:
                    z = 0
                    node_list += "'{}')".format(a.val)
                else:
                    node_list += "'{}', ".format(a.val)
                    a = a.next
            else:
                if not a.next:
                    z = 0
                    node_list += "{})".format(a.val)
                else:
                    node_list += "{}, ".format(a.val)
                    a = a.next
        return node_list

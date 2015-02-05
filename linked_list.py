#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Node(object):

    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            self.head, self.head.next = Node(val), self.head

    def pop(self):
        if not self.head:
            return None
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def size(self):
        i = 0
        a = self.head
        while a:
            i += 1
            a = a.next
        return i

    def search(self, value):
        a = self.head
        while a:
            if a.val == value:
                return a
            else:
                a = a.next
        return None

    def remove(self, node):
        z = 1
        a = self.head
        while z:
            if self.head == node:
                z = 0
                self.head = self.head.next
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
        a = self.head
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

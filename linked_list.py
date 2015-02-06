#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Node(object):

    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, val):
        self.head = Node(val, self.head)

    def pop(self):
        if not self.head:
            return None
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def size(self):
        i = 0
        current = self.head
        while current:
            i += 1
            current = current.next
        return i

    def search(self, value):
        current = self.head
        while current:
            if current.val == value:
                return current
            else:
                current = current.next
        return None

    def remove(self, node):
        current = self.head

        if self.head == node:
            self.head = self.head.next
            return

        while current:
            if current.next == node:
                current.next = node.next
                return
            else:
                current = current.next

    def display(self):
        print(repr(self))

    def __repr__(self):
        current = self.head
        node_list = "("
        while current:
            if isinstance(current.val, str) or isinstance(current.val, unicode):
                node_list += "'{}'".format(current.val)
            else:
                node_list += "{}".format(current.val)

            if not current.next:
                node_list += ")"
                return node_list

            current = current.next

            node_list += ", "

        node_list += ")"
        return node_list

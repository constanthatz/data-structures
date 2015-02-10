#!/usr/bin/env python
from __future__ import unicode_literals


class Node(object):
    ''' Create data Node with default value and next pointer. '''
    def __init__(self, value, ahead=None, behind=None):
        ''' Value and next pointer default to none. '''
        self.val = value
        self.ahead = ahead
        self.behind = behind


class DLL(object):
    ''' Create an empty DLL. '''
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        ''' Add data Node to the tail of DLL. '''
        self.head = Node(value, self.tail)

        if not self.tail:
            self.tail = self.head
        else:
            self.head.behind.ahead = self.head

    def pop(self):
        ''' Remove head Node from head of DLL. Reassign head data
            Node and return value of popped Node. '''
        try:
            val = self.head.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("pop from empty DLL")
        self.head.behind.ahead, self.head = None, self.head.behind
        return val

    def append(self, value):
        ''' Add data Node to the tail of DLL. '''
        self.tail = Node(value, self.tail)

        if not self.head:
            self.head = self.tail
        else:
            self.tail.ahead.behind = self.tail

    def shift(self):
        ''' Remove tail Node from tail of DLL. Reassign tail data
            Node and return value of shifted Node. '''
        try:
            val = self.tail.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("shift from empty DLL")
        self.tail.ahead.behind, self.tail = None, self.tail.ahead
        return val

    def remove(self, val):
        ''' Remove a given value from the DLL '''
        current = self.head

        if self.head.val == val:
            # test if we are the head node
            self.head = self.head.behind
            return

        while current.behind:
            if (current.behind == self.tail) and (self.tail == val):
                self.tail = self.tail.ahead
                return
            elif current.behind.val == val:
                current.behind.behind.ahead = current.behind.ahead
                return
            else:
                current = current.behind
        raise ValueError("dll.remove(val): val not in list")

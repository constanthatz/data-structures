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
        self.tail = Node(value, self.tail)

        if not self.head:
            self.head = self.tail
        else:
            self.tail.ahead.behind = self.tail

    def pop():
        ''' Remove head Node from head of DLL. Reassign head data
            Node and return value of deDLLd Node. '''
        try:
            val = self.head.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("deDLL from empty Stack")
        self.head.behind.ahead, self.head = None, self.head.behind
        return val

    def append(self, value):
        ''' Add data Node to the tail of DLL. '''
        self.tail = Node(value, self.tail)

        if not self.head:
            self.head = self.tail
        else:
            self.tail.ahead.behind = self.tail

    def shift():
        ''' Remove head Node from head of DLL. Reassign head data
            Node and return value of deDLLd Node. '''
        try:
            val = self.head.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("deDLL from empty Stack")
        self.head.behind.ahead, self.head = None, self.head.behind
        return val

    def size(self):
        ''' Return size of DLL (number of Nodes). '''
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.ahead
        return count

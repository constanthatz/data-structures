#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    ''' Create data element with default value and previous pointer. '''
    def __init__(self, value, previous=None):
        ''' Value and previous pointer default to none. '''
        self.val = value
        self.previous = previous


class Stack(object):
    ''' Create an empty stack. '''
    def __init__(self):
        self.top = None

    def push(self, value):
        ''' Add data element to the top of stack. '''
        self.top = Element(value, self.top)

    def pop(self):
        ''' Remove top element from stack. Reassign and reassign top data
            element. '''
        try:
            val = self.top.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("pop from empty Stack")
        self.top = self.top.previous
        return val

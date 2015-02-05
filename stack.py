#!/usr/bin/env python


class Element(object):
    ''' Create data element with default value and previous pointer. '''
    def __init__(self, value=None, previous=None):
        ''' Value and previous pointer default to none. '''
        self.val = value
        self.previous = previous


class Stack(object):
    ''' Create an empty stack. '''
    def __init__(self):
        self.top = None

    def push(self, element):
        ''' Add data element to the top of stack. '''
        self.top, self.top.previous = element, self.top

    def pop(self):
        ''' Remove top element from stack. Reassign and reassign top data
            element. '''
        if not self.top:
            # If no data element to pop it is considered a ValueError.
            raise ValueError
        else:
            val = self.top.val
            self.top = self.top.previous
            return val

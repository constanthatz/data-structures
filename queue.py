#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    ''' Create data element with default value and next pointer. '''
    def __init__(self, value, ahead=None, behind=None):
        ''' Value and next pointer default to none. '''
        self.val = value
        self.ahead = ahead
        self.behind = behind


class Queue(object):
    ''' Create an empty queue. '''
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        ''' Add data element to the back of queue. '''
        self.back.behind = Element(value, self.back)
        self.back = self.back.behind
        if not self.front:
            self.front = self.back

    def dequeue(self):
        ''' Remove front element from front of queue. Reassign front data
            element and return value of dequeued element. '''
        try:
            val = self.front.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("dequeue from empty Stack")
        self.front = self.front.previous
        return val

    def size(self):
        return size

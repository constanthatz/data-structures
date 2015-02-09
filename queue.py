#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    ''' Create data element with default value and next pointer. '''
    def __init__(self, value, next=None):
        ''' Value and next pointer default to none. '''
        self.val = value
        self.next = next


class Queue(object):
    ''' Create an empty queue. '''
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        ''' Add data element to the back of queue. '''
        self.back = Element(value, self.back)

        if not self.front:
            self.front = self.back

    def dequeue(self):
        ''' Remove front element from queue. Reassign front data
            element and return value of dequeued element. '''
        try:
            val = self.front.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("pop from empty Stack")
        self.top = self.top.previous
        return val

    def size(self):
        return size

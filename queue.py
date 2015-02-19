#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    ''' Create data element with default value and next pointer. '''
    def __init__(self, value, behind=None):
        ''' Value and next pointer default to none. '''
        self.val = value
        self.behind = behind


class Queue(object):
    ''' Create an empty queue. '''
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        # Add data element to the back of queue.
        new = Element(value)
        try:
            self.back.behind = new
        except AttributeError:
            self.front = new
        self.back = new

    def dequeue(self):
        ''' Remove front element from front of queue. Reassign front data
            element and return value of dequeued element. '''
        try:
            val = self.front.val
        except AttributeError:
            # Mimic error message from list.
            raise IndexError("dequeue from empty Stack")

        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.behind
        return val

    def size(self):
        ''' Return size of queue (number of elements). '''
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.behind
        return count

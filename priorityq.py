#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    ''' Create data element with default value and next pointer. '''
    def __init__(self, value, ahead=None, behind=None, priority=0):
        ''' Value and next pointer default to none. '''
        self.val = value
        self.ahead = ahead
        self.behind = behind
        self.prio = priority


class Priorityq(object):
    ''' Create an empty queue. '''
    def __init__(self):
        self.front = None
        self.back = None

    def insert(self, value):
        ''' Add data element to the back of queue. '''
        self.back = Element(value, self.back)

        if not self.front:
            self.front = self.back
        else:
            self.back.ahead.behind = self.back

    def __sort(self):
        return

    def dequeue(self):
        ''' Remove front element from front of queue. Reassign front data
            element and return value of dequeued element. '''
        try:
            val = self.front.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("dequeue from empty Stack")
        self.front.behind.ahead, self.front = None, self.front.behind
        return val

    def size(self):
        ''' Return size of queue (number of elements). '''
        count = 0
        current = self.back
        while current:
            count += 1
            current = current.ahead
        return count

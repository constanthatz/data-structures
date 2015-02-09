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
        self.back = Element(value, self.back)

        if not self.front:
            self.front = self.back
        else:
            self.back.ahead.behind = self.back

    # def dequeue(self):
    #     ''' Remove front element from front of queue. Reassign front data
    #         element and return value of dequeued element. '''
    #     try:
    #         val = self.front.val
    #     except AttributeError:
    #         ''' Mimic error message from list '''
    #         raise IndexError("dequeue from empty Stack")
    #     self.front = self.front.previous
    #     return val

    # def size(self):
    #     return size


x = Queue()

x.enqueue("A")
print(x.front)
print(x.back)
print(x.front.val)
print(x.back.val)
x.enqueue("B")
print(x.front)
print(x.back)
print(x.front.val)
print(x.back.val)
x.enqueue("C")
print(x.front)
print(x.back)
print(x.front.val)
print(x.back.val)
print(x.back.ahead.val)
print(x.front.behind.val)
print(x.front.ahead)
print(x.back.behind)
print(x.back.ahead.behind.val)
x.enqueue("D")
print(x.front)
print(x.back)
print(x.front.val)
print(x.back.val)
print(x.back.ahead.val)
print(x.front.behind.val)
print(x.front.ahead)
print(x.back.behind)
print(x.back.ahead.behind.val)

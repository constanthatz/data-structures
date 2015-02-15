#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    ''' Create data element with default value and next pointer. '''
    def __init__(self, value, priority=0, behind=None):
        ''' Value and next pointer default to none. '''
        self.val = value
        self.behind = behind
        self.prio = priority


class Priorityq(object):
    ''' Create an empty queue. '''
    def __init__(self):
        self.front = None
        self.back = None

    def insert(self, value, priority=0):
        ''' Add data element to the back of queue. '''
        new_element = Element(value, priority)
        current = self.front

        try:
            if new_element.prio > self.front.prio:
                new_element.behind, self.front = self.front, new_element
                return
        except AttributeError:
            self.front = new_element
            return

        current = self.front

        while True:
            try:
                if new_element.prio <= current.behind.prio:
                    current = current.behind
                else:
                    new_element.behind, current.behind = current.behind, new_element
                    return
            except AttributeError:
                current.behind = new_element
                return

    def pop(self):
        ''' Return value of highest priority element and remove. '''
        if not self.front:
            raise IndexError('pop from empty queue')
        elif not self.front.behind:
            pop_value = self.front.val
            self.back = self.front = None
            return pop_value
        else:
            pop_value = self.front.val
            self.front = self.front.behind
            return pop_value

    def peek(self):
        ''' Return value of highest priority element. '''
        if not self.front:
            raise IndexError('peek from empty queue')
        else:
            return self.front.val

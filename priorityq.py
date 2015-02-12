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
        new_element = Element(value, self.back)

        if not self.front:
            self.front = self.back = new_element
        elif new_element.prio <= self.back.prio:
            new_element.ahead, self.back = self.back, new_element
        else:
            self.__prioritize(new_element)

    def __prioritize(self, new_element):

        current = self.back.ahead

        while True:
            if new_element.prio <= current.prio:
                new_element.behind = current
                new_element.ahead.behind.ahead = new_element
                new_element.behind = new_element.ahead.behind
                new_element.ahead.behind = new_element
                return
            else:
                try:
                    current = current.ahead
                except AttributeError:
                    new_element.behind, self.front = self.front, new_element
                    return

    def pop(self):
        pop_value = self.front
        self.front.behind.ahead, self.front = None, self.front.behind
        return pop_value

#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    ''' Create data element with default value and next pointer. '''
    def __init__(self, value, priority=0, ahead=None, behind=None):
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

    def insert(self, value, priority=0):
        ''' Add data element to the back of queue. '''
        new_element = Element(value, priority)
        if not self.front:
            self.front = self.back = new_element
        elif new_element.prio <= self.back.prio:
            new_element.ahead, self.back = self.back, new_element
        else:
            self.__prioritize(new_element)

    def __prioritize(self, new_element):
        ''' Insert new element into the right place in the queue based on
            priority and order entered. '''
        current = self.back.ahead

        while True:
            print(type(new_element))
            print(type(current))

            if new_element.prio <= current.prio:
                # Insert element and reassingn all pointers
                new_element.behind = current
                new_element.ahead.behind.ahead = new_element
                new_element.behind = new_element.ahead.behind
                new_element.ahead.behind = new_element
                return
            else:
                # Move to next element

                if not current.ahead:
                    new_element.behind, self.front = self.front, new_element
                    return
                else:
                    current = current.ahead

    def pop(self):
        ''' Return value of highest priority element and remove. '''
        pop_value = self.front
        self.front.behind.ahead, self.front = None, self.front.behind
        return pop_value

    def peek(self):
        ''' Return value of highest priority element. '''
        return self.front

if __name__ == '__main__':
    l = Priorityq()
    l.insert("Nick", 1)
    assert l.front.val == "Nick"
    assert l.back.val == "Nick"

    l.insert("Constantine", 1)
    assert l.front.val == "Nick"
    assert l.back.val == "Constantine"

    l.insert("Mark", 2)
    assert l.front.val == "Mark"
    assert l.back.val == "Constantine"

    l.insert("Henry", 2)
    l.insert("Jake", 3)
    l.insert("James", 0)

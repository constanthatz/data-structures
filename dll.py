#!/usr/bin/env python
from __future__ import unicode_literals


class Node(object):
    ''' Create data Node with default value and next pointer. '''
    def __init__(self, value, ahead=None, behind=None):
        ''' Value and next pointer default to none. '''
        self.val = value
        self.ahead = ahead
        self.behind = behind


class DLL(object):
    ''' Create an empty DLL. '''
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        ''' Add data Node to the head of DLL. '''
        self.head = Node(value, behind=self.head)

        if not self.tail:
            self.tail = self.head
        else:
            self.head.behind.ahead = self.head

    def pop(self):
        ''' Remove head Node from head of DLL. Reassign head data
            Node and return value of popped Node. '''
        try:
            val = self.head.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("pop from empty DLL")
        self.head.behind.ahead, self.head = None, self.head.behind
        return val

    def append(self, value):
        ''' Add data Node to the tail of DLL. '''
        self.tail = Node(value, self.tail)

        if not self.head:
            self.head = self.tail
        else:
            self.tail.ahead.behind = self.tail

    def shift(self):
        ''' Remove tail Node from tail of DLL. Reassign tail data
            Node and return value of shifted Node. '''
        try:
            val = self.tail.val
        except AttributeError:
            ''' Mimic error message from list '''
            raise IndexError("shift from empty DLL")
        self.tail.ahead.behind, self.tail = None, self.tail.ahead
        return val

    def remove(self, val):
        ''' Remove a given value from the DLL '''
        current = self.head

        try:
            if self.head.val == val:
                self.head = self.head.behind
                return
            # test if we are the head node
        except AttributeError:
            raise ValueError("dll.remove(val): val not in list")

        current = current.behind

        print(current.val)
        while current:
            print(current.val)
            if current.val == val:
                print(current.val)
                current.behind.ahead = current.ahead
                current.ahead.behind = current.behind
                return
            else:
                current = current.behind

        if current.ahead.val == val:
            self.tail = self.tail.ahead
        else:
            raise ValueError("dll.remove(val): val not in list")

if __name__ == '__main__':
    ''' Test remove method. '''
    l = DLL()

    ''' Test remove on non-empty dll. '''
    l.insert(10)
    l.insert("String")
    l.insert(5)
    l.insert("Other")
    l.insert([1, "string"])

    ''' Test removing middle '''
    l.remove(5)
    print(l.tail.val)
    print(l.tail.ahead.val)
    print(l.tail.ahead.ahead.val)
    print(l.head.behind.behind.val)

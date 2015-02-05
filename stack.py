#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Element(object):

    def __init__(self, value=None, previous=None):
        self.val = value
        self.previous = next


class Stack(object):

    def __init__(self):
        self.top = None

    def push(self, element):
        self.top, self.top.previous = element, self.top

    def pop(self):
        if not self.top:
            ''' No element to pop is considered a ValueError '''
            raise ValueError
        else:
            val = self.top.val
            self.top = self.top.previous
            return val

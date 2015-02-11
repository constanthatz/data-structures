#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Binheap(object):
    ''' Create an empty heap. '''
    def __init__(self, binlist=[]):
        self.binlist = binlist

    def push(self, value):
        self.binlist.append[value]
        return

    def pop(self):
        return self.binlist.pop([0])

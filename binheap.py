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
        top = self.binlist[0]
        if self.binlist[2] >= self.binlist[1]:
            self.binlist[0] = self.binlist[2]
        else:
            self.binlist[0] = self.binlist[1]
        return top

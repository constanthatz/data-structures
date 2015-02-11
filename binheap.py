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
            empty_bin = 2
        else:
            self.binlist[0] = self.binlist[1]
            empty_bin = 1

        self.__resort(empty_bin)
        return top

    def __resort(self, empty_bin):
        child1 = 2*empty_bin+1
        child2 = 2*empty_bin+2

        if self.binlist[child2] >= self.binlist[child1]:
            self.binlist[empty_bin] = self.binlist[child2]
        else:
            self.binlist[empty_bin] = self.binlist[child1]
        return


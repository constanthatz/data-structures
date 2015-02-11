#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division


class Binheap(object):
    ''' Create an empty heap. '''
    def __init__(self, binlist=[]):
        self.binlist = binlist

    def push(self, value):
        self.binlist.append[value]
        self.__promote()
        return

    def __promote(self):
        return


    def __parent(self, index):
        parent = [(index-1)//2, self.binlist[(index-1)//2]]


    def __children(self, index):
        parent = [(2*index+1, self.binlist[2*index+1]), ((2*index+2, self.binlist[2*index+2]))]
        return


    def __swap():
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

        try:
            while self.binlist[child2] or self.binlist[child1]:
                if self.binlist[child2] >= self.binlist[child1]:
                    self.binlist[empty_bin] = self.binlist[child2]
                    empty_bin = child2
                else:
                    self.binlist[empty_bin] = self.binlist[child1]
                    empty_bin = child1

                child1 = 2*empty_bin+1
                child2 = 2*empty_bin+2
                return

        except IndexError:
            return

#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division


class Binheap(object):
    ''' Create an empty heap. '''
    def __init__(self, binlist=[]):
        self.binlist = binlist

    def push(self, value):
        self.binlist.append(value)
        self.__promote(len(self.binlist)-1)
        return

    def __promote(self, index):
        child = self.binlist[index]
        parent = self.__parent(index)
        print(parent)
        if parent[0] >= 0:
            if parent[1] < child:
                self.__swap(parent[0], index)
                self.__promote(parent[0])
            else:
                return

    def __parent(self, index):
        parent = [(index-1)//2, self.binlist[(index-1)//2]]
        return parent

    def __children(self, index):
        children = [(2 * index + 1, self.binlist[2*index+1]), ((2*index+2, self.binlist[2*index+2]))]
        return

    def __swap(self, index1, index2):
        self.binlist[index1], self.binlist[index2] = self.binlist[index2], self.binlist[index1]
        return

    def __battle_children(self, index, children):
        child1 = children[0]
        child2 = children[1]
        if child1[1] >= child2[1]:
            self.__swap(child1[0], index)
            return child1[0]
        else:
            self.__swap(child2[0], index)
            return child2[0]

    def pop(self):
        top = self.binlist[0]
        index = 0
        try:
            while self.__children(index):
                children = self.__children(index)
                index = self.__battle_children(index, children)
        except IndexError:
            return top


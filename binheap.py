#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division


class Binheap(object):
    ''' Create an empty heap. '''
    def __init__(self, binlist=[]):
        self.binlist = binlist

    def push(self, value):
        ''' Add a value to the heap. '''
        self.binlist.append(value)
        self.__promote(len(self.binlist)-1)
        return

    def __parent(self, index):
        ''' Find the parents of a bin. '''
        parent = [(index-1)//2, self.binlist[(index-1)//2]]
        return parent

    def __children(self, index):
        ''' Find the children of a bin. '''
        children = []
        try:
            child1 = (2 * index + 1, self.binlist[2*index+1])
        except IndexError:
            pass
        else:
            children.append(child1)

        try:
            child2 = (2*index+2, self.binlist[2*index+2])
        except IndexError:
            pass
        else:
            children.append(child2)

        return children

    def __swap(self, index1, index2):
        ''' Swap two bins. '''
        self.binlist[index1], self.binlist[index2] = self.binlist[index2], self.binlist[index1]
        return

    def pop(self):
        ''' Pop the top of the heap. '''
        last_index = len(self.binlist)-1
        self.__swap(0, last_index)
        top = self.binlist.pop()
        self.__demote()
        return top

    def __promote(self, index):
        ''' Promote a bin. '''
        child = self.binlist[index]
        parent = self.__parent(index)
        if parent[0] >= 0:
            if parent[1] < child:
                self.__swap(parent[0], index)
                self.__promote(parent[0])
            else:
                return

    def __demote(self, index=0):
        children = self.__children(index)
        ''' Demote a bin. '''
        if len(children):
            victor_index = self.__battle_children(index, children)

            if victor_index:
                self.__swap(victor_index, index)
                self.__demote(victor_index)
        else:
            return

    def __battle_children(self, index, children):
        ''' Compare children bins. '''
        if len(children) == 2:
            child1 = children[0]
            child2 = children[1]

            if child1[1] >= child2[1]:
                return child1[0]
            else:
                return child2[0]

        elif len(children) == 1:
            child = children[0]
            return child[0]
        else:
            return None

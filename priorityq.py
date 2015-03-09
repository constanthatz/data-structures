#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    ''' Create data element with default value and next pointer. '''
    def __init__(self, value, priority=0):
        ''' Value and next pointer default to none. '''
        self.val = value
        self.prio = priority


class Priorityq(object):
    ''' Create an empty heap. '''
    def __init__(self):
        self.binlist = []

    def insert(self, value, priority=0):
        ''' Add a value to the heap. '''
        self.binlist.append(Element(value, priority))
        self._promote(len(self.binlist)-1)
        return

    def _parent(self, index):
        ''' Find the parents of a bin. '''
        return [(index-1)//2, self.binlist[(index-1)//2].prio]

    def _children(self, index):
        ''' Find the children of a bin. Build list of children. '''
        children = []
        try:
            child1 = (2 * index + 1, self.binlist[2*index+1].prio)
        except IndexError:
            pass
        else:
            children.append(child1)

        try:
            child2 = (2*index+2, self.binlist[2*index+2].prio)
        except IndexError:
            pass
        else:
            children.append(child2)

        return children

    def _swap(self, index1, index2):
        ''' Swap two bins. '''
        self.binlist[index1], self.binlist[index2] = self.binlist[index2], self.binlist[index1]
        return

    def pop(self):
        ''' Pop the top of the heap. '''
        last_index = len(self.binlist)-1
        top = self.binlist[0].val
        self._swap(0, last_index)
        self.binlist.pop()
        self._demote()
        return top

    def peek(self):
        ''' Return value of highest priority element. '''
        try:
            return self.binlist[0].val
        except AttributeError:
            raise IndexError('peek from empty queue')

    def _promote(self, index):
        ''' Promote a bin. '''
        child = self.binlist[index].prio
        parent = self._parent(index)
        if parent[0] >= 0:
            # If is true only when parent index is non-negative
            if parent[1] < child:
                self._swap(parent[0], index)
                self._promote(parent[0])
            else:
                return

    def _demote(self, index=0):
        children = self._children(index)
        ''' Demote a bin. '''
        if len(children):
            victor_index = self._battle_children(index, children)

            if victor_index:
                self._swap(victor_index, index)
                self._demote(victor_index)
        else:
            return

    def _battle_children(self, index, children):
        ''' Compare children bins. '''
        if len(children) == 2:
            # Handle two children
            if children[0][1] >= children[1][1]:
                return children[0][0]
            else:
                return children[1][0]

        elif len(children) == 1:
            # Handle one child
            return children[0][0]
        else:
            # Handle no children
            return None

if __name__ == '__main__':
    pqueue = Priorityq()
    print(len(pqueue.binlist))
    pqueue.insert("Nick", 5)
    print(len(pqueue.binlist))
    for i in pqueue.binlist:
        print(i.val)
    pqueue.insert("Constantine", 1)
    print(len(pqueue.binlist))
    for i in pqueue.binlist:
        print(i.val)

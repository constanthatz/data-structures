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
    def __init__(self, binlist=[]):
        self.binlist = binlist

    def push(self, value):
        ''' Add a value to the heap. '''
        self.binlist.append(Element(value, priority=0))
        self.__promote(len(self.binlist)-1)
        return

    def __parent(self, index):
        ''' Find the parents of a bin. '''
        return [(index-1)//2, self.binlist[(index-1)//2].prio]

    def __children(self, index):
        ''' Find the children of a bin. Build list of children. '''
        children = []
        try:
            child1 = (2 * index + 1, self.binlist[2*index+1].prio)
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
        return top.val

    def __promote(self, index):
        ''' Promote a bin. '''
        child = self.binlist[index]
        parent = self.__parent(index)
        if parent[0] >= 0:
            # If is true only when parent index is non-negative
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


# class Priorityq(object):
#     ''' Create an empty queue. '''
#     def __init__(self):
#         self.front = None
#         self.back = None

#     def insert(self, value, priority=0):
#         ''' Add data element to the back of queue. '''
#         new_element = Element(value, priority)
#         current = self.front

#         try:
#             if new_element.prio > self.front.prio:
#                 new_element.behind, self.front = self.front, new_element
#                 return
#         except AttributeError:
#             self.front = new_element
#             return

#         current = self.front

#         while True:
#             try:
#                 if new_element.prio <= current.behind.prio:
#                     current = current.behind
#                 else:
#                     new_element.behind, current.behind = current.behind, new_element
#                     return
#             except AttributeError:
#                 current.behind = new_element
#                 return

#     def pop(self):
#         ''' Return value of highest priority element and remove. '''

#         try:
#             pop_value, self.front = self.front.val, self.front.behind
#             return pop_value
#         except AttributeError:
#             raise IndexError('pop from empty queue')

#     def peek(self):
#         ''' Return value of highest priority element. '''
#         try:
#             return self.front.val
#         except AttributeError:
#             raise IndexError('peek from empty queue')

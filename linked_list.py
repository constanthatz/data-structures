#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Node(object):
    ''' Create node element with default previous pointer. '''
    def __init__(self, value, next=None):
        ''' Previous pointer default to none. '''
        self.val = value
        self.next = next


class LinkedList(object):
    ''' Create an empty linked list. '''
    def __init__(self):
        self.head = None

    def insert(self, val):
        ''' Add node to the top of head of list. '''
        self.head = Node(val, self.head)

    def pop(self):
        ''' Remove head node from list. Reassign and reassign head node. '''
        if not self.head:
            return None
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def size(self):
        ''' Return size of list (number of nodes). '''
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, value):
        ''' Return node with the given value. '''
        current = self.head
        while current:
            if current.val == value:
                return current
            else:
                current = current.next
        return None

    def remove(self, node):
        ''' Remove node from list. '''
        current = self.head

        if self.head == node:
            # test if we are the head node
            self.head = self.head.next
            return

        while current:
            if current.next == node:
                current.next = node.next
                return
            else:
                current = current.next

    def display(self):
        ''' Print list to console. '''
        print(repr(self))

    def __repr__(self):
        current = self.head
        node_list = "("
        while current:
            if isinstance(current.val, str) or isinstance(current.val, unicode):
                node_list += "'{}'".format(current.val)
            else:
                node_list += "{}".format(current.val)

            if not current.next:
                node_list += ")"
                return node_list

            current = current.next

            node_list += ", "

        node_list += ")"
        return node_list

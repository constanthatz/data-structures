class Node(object):

    def __init__(self, val):
        self.val = val
        self._next = None

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, value):
            self._next = value


class LinkedList(object):

    def __init__(self, name):
        self.head = None
        self.second = None

    def insert(self, val):
        self.second, self.head = self.head, Node(val)
        self.head.next = self.second


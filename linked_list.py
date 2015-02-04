class Node(object):

    def __init__(self, val):
        self.val = val
        self._next = None

        @property
        def next(self):
            return self._next

        @next.setter
        def name(self, value):
            self._next = value


class LinkedList(object):

    def __init__(self, name):
        self.head = None
        self.active = None

    def insert(self, val):
        self.active, self.head = self.head, Node(val)
        self.head.next = self.active

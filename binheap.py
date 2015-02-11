#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Binheap(object):
    ''' Create an empty heap. '''
    def __init__(self, list=[]):
        self.list = list

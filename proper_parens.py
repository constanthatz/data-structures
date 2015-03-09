#!/usr/bin/env python
from __future__ import unicode_literals
from stack import Element, Stack


def check_statement(value):
    ''' Return 1, 0, or -1 if input is open, balanced, or broken. '''
    S = Stack()
    balanced = True
    index = 0
    while index < len(value) and balanced:
        character = value[index]
        if character == "(":
            S.push(Element(character))
        else:
            if not S.top:
                return -1
            else:
                S.pop()

        index = index + 1

    if balanced and not S.top:
        return 0
    else:
        return 1
